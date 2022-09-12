"""
VBI l0_pipeline workflow.

This workflow is used when raw L0 VBI data was delivered to the DKIST Data Center for calibration.

DKIST: https://nso.edu/telescopes/dki-solar-telescope/

VBI: https://nso.edu/telescopes/dkist/instruments/vbi/

This workflow does *not* include the speckle reconstruction algorithms used in summit-calibrated data.
Instead, darks and gains are generated by averaging the raw darks and gains, and are then subtracted from the science frames.
"""
from dkist_processing_common.tasks import AddDatasetReceiptAccount
from dkist_processing_common.tasks import PublishCatalogAndQualityMessages
from dkist_processing_common.tasks import QualityL1Metrics
from dkist_processing_common.tasks import SubmitQuality
from dkist_processing_common.tasks import Teardown
from dkist_processing_common.tasks import TransferL0Data
from dkist_processing_common.tasks import TransferL1Data
from dkist_processing_core import Workflow

from dkist_processing_vbi.tasks.assemble_movie import AssembleVbiMovie
from dkist_processing_vbi.tasks.dark import DarkCalibration
from dkist_processing_vbi.tasks.gain import GainCalibration
from dkist_processing_vbi.tasks.make_movie_frames import MakeVbiMovieFrames
from dkist_processing_vbi.tasks.parse import ParseL0VbiInputData
from dkist_processing_vbi.tasks.quality_metrics import VbiQualityL0Metrics
from dkist_processing_vbi.tasks.quality_metrics import VbiQualityL1Metrics
from dkist_processing_vbi.tasks.science import ScienceCalibration
from dkist_processing_vbi.tasks.write_l1 import VbiWriteL1Frame

l0_pipeline = Workflow(
    input_data="l0",
    output_data="l1",
    category="vbi",
    detail="no-speckle",
    workflow_package=__package__,
)

l0_pipeline.add_node(task=TransferL0Data, upstreams=None)
l0_pipeline.add_node(task=ParseL0VbiInputData, upstreams=TransferL0Data)
l0_pipeline.add_node(task=VbiQualityL0Metrics, upstreams=ParseL0VbiInputData)
l0_pipeline.add_node(task=DarkCalibration, upstreams=ParseL0VbiInputData)
l0_pipeline.add_node(task=GainCalibration, upstreams=DarkCalibration)
l0_pipeline.add_node(task=ScienceCalibration, upstreams=GainCalibration)
l0_pipeline.add_node(task=VbiWriteL1Frame, upstreams=ScienceCalibration)
l0_pipeline.add_node(task=MakeVbiMovieFrames, upstreams=VbiWriteL1Frame)
l0_pipeline.add_node(task=AssembleVbiMovie, upstreams=MakeVbiMovieFrames)
l0_pipeline.add_node(task=QualityL1Metrics, upstreams=VbiWriteL1Frame)
l0_pipeline.add_node(task=VbiQualityL1Metrics, upstreams=VbiWriteL1Frame)
l0_pipeline.add_node(
    task=SubmitQuality, upstreams=[VbiQualityL0Metrics, QualityL1Metrics, VbiQualityL1Metrics]
)
l0_pipeline.add_node(task=AddDatasetReceiptAccount, upstreams=[AssembleVbiMovie, SubmitQuality])
l0_pipeline.add_node(task=TransferL1Data, upstreams=AddDatasetReceiptAccount)
l0_pipeline.add_node(
    task=PublishCatalogAndQualityMessages,
    upstreams=TransferL1Data,
)
l0_pipeline.add_node(task=Teardown, upstreams=PublishCatalogAndQualityMessages)
