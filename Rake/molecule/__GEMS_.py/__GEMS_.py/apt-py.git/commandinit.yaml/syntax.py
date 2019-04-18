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

from molecule import logger
from molecule import scenarios
from molecule.command import base

LOG = logger.get_logger(__name__)


class Syntax(base.Base):
    """
    .. program:: molecule syntax

    .. option:: molecule syntax

        Target the default scenario.

    .. program:: molecule syntax --scenario-name foo

    .. option:: molecule syntax --scenario-name foo

<<<<<<< HEAD:molecule/command/syntax.py
        Targeting a specific scenario.

    .. program:: molecule --debug syntax

    .. option:: molecule --debug syntax

        Executing with `debug`.

    .. program:: molecule --base-config base.yml syntax

    .. option:: molecule --base-config base.yml syntax

        Executing with a `base-config`.

    .. program:: molecule --env-file foo.yml syntax

    .. option:: molecule --env-file foo.yml syntax

        Load an env file to read variables from when rendering
        molecule.yml.
=======
    $ molecule --debug syntax
>>>>>>> b1eb06d375fd544a849fcf5c39f51dc334b87338:Rake/molecule/__GEMS_.py/__GEMS_.py/apt-py.git/commandinit.yaml/syntax.py
    """

    def execute(self):
        """
        Execute the actions necessary to perform a `molecule syntax` and
        returns None.

        :return: None
        """
        self.print_info()
        self._config.provisioner.syntax()


@click.command()
@click.pass_context
@click.option(
    '--scenario-name',
    '-s',
    default=base.MOLECULE_DEFAULT_SCENARIO_NAME,
    help='Name of the scenario to target. ({})'.format(
        base.MOLECULE_DEFAULT_SCENARIO_NAME))
def syntax(ctx, scenario_name):  # pragma: no cover
    """ Use the provisioner to syntax check the role. """
    args = ctx.obj.get('args')
    subcommand = base._get_subcommand(__name__)
    command_args = {
        'subcommand': subcommand,
    }

    s = scenarios.Scenarios(
        base.get_configs(args, command_args), scenario_name)
    s.print_matrix()
    for scenario in s:
        for action in scenario.sequence:
            scenario.config.action = action
            base.execute_subcommand(scenario.config, action)
