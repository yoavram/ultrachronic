from ultrachronic import jsonify_result, repeat

import click
from click.testing import CliRunner

@jsonify_result
def simulation(arg1, arg2):
	a = 1
	b = 2
	return dict(a=a, b=b)

def test_ultrachronic():
	@click.command()
	@click.option('--arg1', default=1, type=int, help='Argument 1')
	@click.option('--arg2', default='a', type=str, help='Argument 2')
	@click.option('--reps', default=1, type=int, help='Number of repetitions')
	def main(arg1, arg2, reps):
		repeat(simulation, reps, arg1=arg1, arg2=arg2)

	runner = CliRunner()
	with runner.isolated_filesystem():
		result = runner.invoke(main, ['--arg1', '1', '--arg2', '2', '--reps', '3'])
	assert result.exit_code == 0

def test_ultrachronic_2_cpus():
	@click.command()
	@click.option('--arg1', default=1, type=int, help='Argument 1')
	@click.option('--arg2', default='a', type=str, help='Argument 2')
	@click.option('--reps', default=1, type=int, help='Number of repetitions')
	def main(arg1, arg2, reps):
		repeat(simulation, reps, cpus=2, arg1=arg1, arg2=arg2)

	runner = CliRunner()
	with runner.isolated_filesystem():
		result = runner.invoke(main, ['--arg1', '1', '--arg2', '2', '--reps', '3'])
	assert result.exit_code == 0

def test_ultrachronic_1_cpu():
	@click.command()
	@click.option('--arg1', default=1, type=int, help='Argument 1')
	@click.option('--arg2', default='a', type=str, help='Argument 2')
	@click.option('--reps', default=1, type=int, help='Number of repetitions')
	def main(arg1, arg2, reps):
		repeat(simulation, reps, cpus=1, arg1=arg1, arg2=arg2)

	runner = CliRunner()
	with runner.isolated_filesystem():
		result = runner.invoke(main, ['--arg1', '1', '--arg2', '2', '--reps', '3'])
	assert result.exit_code == 0

if __name__ == '__main__':
	test_ultrachronic()
