def example(world_one, world_two=None):
    return world_one + world_two


a = 'Hi'
b = 'World2'

# result = example('Hi', 'World')
# result = example(a, b)
result = example(a, world_two=b)

print(result)
