
def is_valid_ipv4(address: str) -> bool:

    numeri: list[str] = address.split('.')
    print(numeri)
    if len(numeri) != 4:
        return False

    for i in numeri:
        if not i.isdigit():
            return False
        i = int(i)
        if 0 <= i <=255:
            continue
        else:
            return False
        
    return True

if __name__ == "__main__":


    print(is_valid_ipv4("592.58.02.14"))
    print(is_valid_ipv4("192.168.0.1"))
    print(is_valid_ipv4("256.100.10.1"))
    print(is_valid_ipv4("192.168.1"))
    print(is_valid_ipv4("192.168.1.a"))