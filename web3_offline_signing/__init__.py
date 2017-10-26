from __future__ import absolute_import

import pkg_resources

from web3_offline_signing.account import Account
from web3_offline_signing.main import Web3
from web3_offline_signing.providers.rpc import (
    HTTPProvider,
)
from web3_offline_signing.providers.tester import (
    TestRPCProvider,
    EthereumTesterProvider,
)
from web3_offline_signing.providers.ipc import (
    IPCProvider,
)

__version__ = pkg_resources.get_distribution("web3").version

__all__ = [
    "__version__",
    "Web3",
    "HTTPProvider",
    "IPCProvider",
    "TestRPCProvider",
    "EthereumTesterProvider",
    "Account",
]
