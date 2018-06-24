import bonobo

# data source (extract the data)
def generate_data():
  yield 'foo'
  yield 'bar'
  yield 'baz'

# transform the data
def uppercase(x: str):
  return x.upper()

# load the data
def output(x: str):
  print(x)

graph = bonobo.Graph(
  generate_data,
  uppercase,
  output,
)

if __name__ == '__main__':
  bonobo.run(graph)