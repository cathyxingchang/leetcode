class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_list = address.split('.')
        defanged_address = '[.]'.join(address_list)
        return defanged_address


s = Solution()
print(s.defangIPaddr("1.1.1.1"))