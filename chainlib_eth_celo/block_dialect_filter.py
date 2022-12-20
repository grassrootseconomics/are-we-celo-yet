from chainlib.dialect import DialectFilter as BaseDialectFilter

class CeloBlockDialectFilter(BaseDialectFilter):
    def apply_src(self, src):
        src['gas_limit'] = '0x0'
        return src
    