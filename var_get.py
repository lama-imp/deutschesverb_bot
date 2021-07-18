import os

with open('reset_original_vars.sh', 'w') as f:
    for var in ['DOCKER_BUILDKIT', 'COMPOSE_DOCKER_CLI_BUILD']:
        docker_var = os.getenv(var)
        if docker_var is not None:
            f.write('export {}={}\n'.format(var, docker_var))
        else:
            f.write('unset {}\n'.format(var))
