from web3_offline_signing.module import (
    Module,
)


class Net(Module):
    @property
    def listening(self):
        return self.web3_offline_signing.manager.request_blocking("net_listening", [])

    @property
    def peerCount(self):
        return self.web3_offline_signing.manager.request_blocking("net_peerCount", [])

    @property
    def version(self):
        return self.web3_offline_signing.manager.request_blocking("net_version", [])