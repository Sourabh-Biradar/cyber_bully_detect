from pathlib import Path
from cybulde.utils.utils import get_logger,run_shell_command

DATA_UTILS_LOGGER = get_logger(Path(__file__).name)


def is_dvc_initilaized() -> bool:
    return (Path().cwd()/".dvc").exists()


def initilaize_dvc() -> None:
    if is_dvc_initilaized():
        DATA_UTILS_LOGGER.info("DVC already initilaized")
        return
    DATA_UTILS_LOGGER.info("intializing DVC")
    run_shell_command("dvc init")
    run_shell_command("dvc config core.analytics false")
    run_shell_command("dvc config core.autostage true")
    run_shell_command("git add .dvc")
    run_shell_command("git commit -nm 'intialized DVC'")