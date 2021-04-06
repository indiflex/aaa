class F:
  def __init__(self, fname):
    self.fname = fname

  def __enter__(self):
    self.file = open(self.fname, 'w')
    return self.file

  def __exit__(self):
    if self.file:
      self.file.close()