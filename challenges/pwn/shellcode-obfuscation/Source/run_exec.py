from execute_input import drop_perms
def run(input:str) -> bytes:
    drop_perms()
    return bytes(eval(input,dict(),dict()))


if __name__ == "__main__":
    print(run(input()))
