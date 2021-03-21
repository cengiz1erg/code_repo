def counter(fn):
    """Bu fonksiyon bir 'decorator' olup çıkışa "inner" adında bir 'closure' iletir. İçerdeki inner fonksiyonu,
    kullanılacak asıl fonksiyonları modifiye eder. Burada modifiye olayı kullanılan fonksiyonun kaçıncı defa
    çağırıldığını ekrana basma'dır. """
    count = 0

    def inner(*args, **kwargs):  # "positional" ve "keyword" değişkenleri paketle
        nonlocal count  # dış fonksiyondaki count etiketinin referansına ulaş
        count += 1
        print(f'{fn.__name__} fonksiyonu {count}. defa çağırılıyor')
        return fn(*args, **kwargs)  # paketlenmiş değişkenleri ayıkla ve fonksiyona girdirt
    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


#-----------
add = counter(add)
mult = counter(mult)
#-----------
