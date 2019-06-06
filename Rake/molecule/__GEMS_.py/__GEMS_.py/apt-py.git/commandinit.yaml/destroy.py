#  Copyright (c) 2015-2017 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import click

from molecule import config
from molecule import logger
from molecule import scenarios
from molecule.command import base

LOG = logger.get_logger(__name__)


class Destroy(base.Base):
    """
    .. program:: molecule destroy

    .. option:: molecule destroy

        Target the default scenario.

    .. program:: molecule destroy --scenario-name foo

    .. option:: molecule destroy --scenario-name foo

        Targeting a specific scenario.

    .. program:: molecule destroy --all

    .. option:: molecule destroy --all

        Target all scenarios.

<<<<<<< HEAD
<<<<<<< HEAD:Rake/molecule/__GEMS_.py/__GEMS_.py/apt-py.git/commandinit.yaml/destroy.py
    $ molecule --debug destroy
=======
=======
<<<<<<< HEAD:molecule/command/destroy.py
>>>>>>> e91355cf081d9dcd78efe38cdcc6f0353a1aa3ac
    .. program:: molecule destroy --driver-name foo

    .. option:: molecule destroy --driver-name foo

        Targeting a specific driver.

    .. program:: molecule --debug destroy

    .. option:: molecule --debug destroy

        Executing with `debug`.

    .. program:: molecule --base-config base.yml destroy

    .. option:: molecule --base-config base.yml destroy

        Executing with a `base-config`.

    .. program:: molecule --env-file foo.yml destroy

    .. option:: molecule --env-file foo.yml destroy

        Load an env file to read variables from when rendering
        molecule.yml.
<<<<<<< HEAD
>>>>>>> 0fa82e7a3daa84ebd03d8af67403c6551113d3e4:molecule/command/destroy.py
=======
=======
    $ molecule --debug destroy
>>>>>>> b1eb06d375fd544a849fcf5c39f51dc334b87338:Rake/molecule/__GEMS_.py/__GEMS_.py/apt-py.git/commandinit.yaml/destroy.py
>>>>>>> e91355cf081d9dcd78efe38cdcc6f0353a1aa3ac
    """

    def execute(self):
        """
        Execute the actions necessary to perform a `molecule destroy` and
        returns None.

        :return: None
        """
        self.print_info()

        if self._config.command_args.get('destroy') == 'never':
            msg = "Skipping, '--destroy=never' requested."
            LOG.warn(msg)
            return

        if self._config.driver.delegated and not self._config.driver.managed:
            msg = 'Skipping, instances are delegated.'
            LOG.warn(msg)
            return

        self._config.provisioner.destroy()
        self._config.state.reset()
        self.prune()


@click.command()
@click.pass_context
@click.option(
    '--scenario-name',
    '-s',
    default=base.MOLECULE_DEFAULT_SCENARIO_NAME,
    help='Name of the scenario to target. ({})'.format(
        base.MOLECULE_DEFAULT_SCENARIO_NAME))
@click.option(
    '--driver-name',
    '-d',
    type=click.Choice(config.molecule_drivers()),
    help='Name of driver to use. (docker)')
@click.option(
    '--all/--no-all',
    '__all',
    default=False,
    help='Destroy all scenarios. Default is False.')
def destroy(ctx, scenario_name, driver_name, __all):  # pragma: no cover
    """ Use the provisioner to destroy the instances. """
    args = ctx.obj.get('args')
    subcommand = base._get_subcommand(__name__)
    command_args = {
        'subcommand': subcommand,
        'driver_name': driver_name,
    }

    if __all:
        scenario_name = None

    s = scenarios.Scenarios(
        base.get_configs(args, command_args), scenario_name)
    s.print_matrix()
    for scenario in s:
        for action in scenario.sequence:
            scenario.config.action = action
            base.execute_subcommand(scenario.config, action)
