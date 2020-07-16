from .bitbucket_repository_provider import BitBucketRepositoryProvider
from .github_repository_provider import GitHubRepositoryProvider
from .github_user_provider import GitHubUserProvider
from .gitlab_repository_provider import GitlabRepositoryProvider
from .gitlab_user_provider import GitlabUserProvider
from .repository_provider import RepositoryProvider

from .channel_provider import ChannelProvider


REPOSITORY_PROVIDERS = [
    BitBucketRepositoryProvider,
    GitHubRepositoryProvider,
    GitHubUserProvider,
    GitlabRepositoryProvider,
    GitlabUserProvider,
    RepositoryProvider
]

CHANNEL_PROVIDERS = [ChannelProvider]
