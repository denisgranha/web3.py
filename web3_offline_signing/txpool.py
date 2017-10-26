from web3_offline_signing.module import (
    Module,
)


class TxPool(Module):
    @property
    def content(self):
        return self.web3_offline_signing.manager.request_blocking("txpool_content", [])

    @property
    def inspect(self):
        return self.web3_offline_signing.manager.request_blocking("txpool_inspect", [])

    @property
    def status(self):
        return self.web3_offline_signing.manager.request_blocking("txpool_status", [])
