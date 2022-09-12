import sys
from functools import lru_cache
from pathlib import Path
from typing import Optional

from pydantic import AnyHttpUrl, BaseSettings, Field, root_validator
from pydantic.error_wrappers import ValidationError

from cluster_agent.identity.slurm_user.constants import (
    LDAPAuthType,
    MapperType,
)
from cluster_agent.utils.logging import logger


class Settings(BaseSettings):
    # slurmrestd info
    BASE_SLURMRESTD_URL: AnyHttpUrl = Field("http://127.0.0.1:6820")
    X_SLURM_USER_NAME: str = "ubuntu"
    X_SLURM_USER_TOKEN: Optional[str]
    DEFAULT_SLURM_WORK_DIR: Path = Path("/tmp")

    # cluster api info
    BASE_API_URL: AnyHttpUrl = Field("https://armada-k8s.staging.omnivector.solutions")

    SENTRY_DSN: Optional[AnyHttpUrl] = None
    SENTRY_ENV: str = "local"

    # OIDC config for machine-to-machine security
    OIDC_DOMAIN: str
    OIDC_AUDIENCE: str = "https://apis.omnivector.solutions"
    OIDC_CLIENT_ID: str
    OIDC_CLIENT_SECRET: str

    CACHE_DIR = Path.home() / ".cache/cluster-agent"

    # Type of slurm user mapper to use
    SLURM_USER_MAPPER: MapperType = MapperType.SINGLE_USER

    # LDAP server settings
    LDAP_HOST: Optional[str]
    LDAP_DOMAIN: Optional[str]
    LDAP_USERNAME: Optional[str]
    LDAP_PASSWORD: Optional[str]
    LDAP_AUTH_TYPE: LDAPAuthType = LDAPAuthType.SIMPLE

    # Single user submitter settings
    SINGLE_USER_SUBMITTER: Optional[str]

    @root_validator
    def compute_extra_settings(cls, values):
        """
        Compute settings values that are based on other settings values.
        """
        ldap_host = values["LDAP_HOST"]
        ldap_domain = values["LDAP_DOMAIN"]

        # Just use the LDAP domain as the host if host is not set but domain is
        if ldap_domain is not None and ldap_host is None:
            values["LDAP_HOST"] = ldap_domain

        # If using single user, but don't have the setting, use default slurm user
        if values["SINGLE_USER_SUBMITTER"] is None:
            values["SINGLE_USER_SUBMITTER"] = values["X_SLURM_USER_NAME"]

        return values

    class Config:
        """
        Provide configuration for the project settings.

        Note that we disable use of ``dotenv`` if we are in test mode.
        """
        env_prefix = "CLUSTER_AGENT_"

        _test_mode = "pytest" in sys.modules
        if not _test_mode:
            env_file = ".env"


@lru_cache()
def init_settings() -> Settings:
    try:
        return Settings()
    except ValidationError as e:
        logger.error(e)
        sys.exit(1)


SETTINGS = init_settings()
