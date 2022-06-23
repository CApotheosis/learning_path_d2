from urllib.parse import urljoin


class A(object):
    def b(self):
        pass

class B(A):
    def b(self):
        return 2

class G(A):
    def b(self):
        return 2

class C(B, G):
    # def mro():
    #     return [C]

    def b(self):
        b = B()

print(NotImplemented)

print(C.mro())


if __name__ == "__main__":
    a = 3 # 8
    a = [] # 
    type("")

    try:
        2/0
    except (Exception) as e:
        print("zero error")
        raise e
