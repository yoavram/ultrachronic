from unittest import TestCase, main

from ultrachronic import jsonify_result, repeat

import click
from click.testing import CliRunner

@jsonify_result
def simulation(arg1, arg2):
	a = 1
	b = 2
	return dict(a=a, b=b)

@click.command()
@click.option('--arg1', default=1, type=int, help='Argument 1')
@click.option('--arg2', default='a', type=str, help='Argument 2')
@click.option('--reps', default=1, type=int, help='Number of repetitions')
@click.option('--cpus', default=1, type=int, help='Number of CPUs')
def command(arg1, arg2, reps, cpus):
	repeat(simulation, reps, cpus=cpus, arg1=arg1, arg2=arg2)

class UCTestCase(TestCase):
	def test_ultrachronic(self):
		runner = CliRunner()
		with runner.isolated_filesystem():
			result = runner.invoke(command, ['--arg1', '1', '--arg2', '2', '--reps', '3'])
		assert result.exit_code == 0, result.exit_code

	def test_ultrachronic_2_cpus(self):
		runner = CliRunner()
		with runner.isolated_filesystem():
			result = runner.invoke(command, ['--arg1', '1', '--arg2', '2', '--reps', '3', '--cpus', '2'])
		assert result.exit_code == 0, result.exit_code

	def test_ultrachronic_1_cpu(self):
		runner = CliRunner()
		with runner.isolated_filesystem():
			result = runner.invoke(command, ['--arg1', '1', '--arg2', '2', '--reps', '3', '--cpus', '1'])
		assert result.exit_code == 0, result.exit_code

if __name__ == '__main__':
	main()
