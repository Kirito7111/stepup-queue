# StepUp Queue integrates queued jobs into a StepUp workflow.
# © 2025 Toon Verstraelen
#
# This file is part of StepUp Queue.
#
# StepUp Queue is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# StepUp Queue is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --
"""StepUp Queue API functions to build workflows."""

from collections.abc import Collection

from stepup.core.api import step
from stepup.core.utils import string_to_list


def sbatch(
    workdir: str,
    *,
    inp: Collection[str] | str = (),
    env: Collection[str] | str = (),
    out: Collection[str] | str = (),
    vol: Collection[str] | str = (),
    optional: bool = False,
    pool: str | None = None,
    block: bool = False,
):
    """Submit a SLURM job script.

    The following filename conventions are used in the given working directory:

    - `job.sh` is the job script to be submitted.
    - `job.log` is StepUp Queue's log file keeping track of the job's status.
    - `job.out` is the job's output file (written by SLURM).
    - `job.err` is the job's error file (written by SLURM).

    Hence, you can only have one job script per working directory,
    and it is strongly recommended to use meaningful directory names.
    Within the directory, try to use as much as possible exactly the same file names for all jobs.

    When the step is executed, it will submit the job or skip this if it was done before.
    If submitted, the step will wait until the job is finished.
    If already finished, the step will essentially be a no-op.

    See `step()` documentation in StepUp Core for all optional arguments.
    and the return value.
    """
    return step(
        "sbatch",
        inp=["slurmjob.sh", *string_to_list(inp)],
        env=env,
        out=["slurmjob.out", "slurmjob.err", *string_to_list(out)],
        vol=["slurmjob.log", *string_to_list(vol)],
        workdir=workdir,
        optional=optional,
        pool=pool,
        block=block,
    )
