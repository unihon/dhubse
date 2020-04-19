# image  is username/repo or library/repo => repo
# name is tag

# image
# can't search repo/name, just kw
DOCKER_IO_API = 'https://index.docker.io/v1/search?q={image}&n={page_size}&page={page}'

# tag
DOCKER_HUB_API = 'https://hub.docker.com/v2/repositories/{image}/tags/?name={name}&page_size={page_size}&page={page}'
