from moto.moto_api import _internal

"""
Global StateManager that everyone uses
Use this manager to configure how AWS models transition between states. (initializing -> starting, starting -> ready, etc.)
"""
state_manager = _internal.state_manager.StateManager()
