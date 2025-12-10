#generator os function with atleast one yield statement. It store the state of the function while iterating through
# generator

def sample_generator():
    yield 1
    yield 2
    yield 3


gen = sample_generator()

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # you will get stop iteration error


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
for num in counter:
    print(num)  # Prints 1 through 5

print("Infite sequence")

def infinte_seq():
    count = 1
    while True:
        yield count
        count+=1

counter = infinte_seq()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


def read_from_file(file_path):
    with open(file_path) as fp:
        for line in fp:
            yield line.strip()

for line in read_from_file("method_overriding.py"):
    if "method" in line:
        print(line)