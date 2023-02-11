from chainlib.dialect import DialectFilter as BaseDialectFilter

class DialectFilter(BaseDialectFilter):
    def apply_block(self, block):
        block.src['gas_limit'] = '0x0'
