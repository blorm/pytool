import sys
import textile

if len(sys.argv) == 1:
  print 'Please input file name:'
  filename = input()
else:
  filename = sys.argv[1]

try:
  f = open(filename, 'r')
except IOError:
  print 'Error: File %s is not accessible.' % filename
  exit()
try:
  f = open(filename + '.html', 'w')
except IOError:
  print 'Error: File %s.html is not accessible.' % filename
  exit()

with open(filename, 'r') as f:
  s = f.read()

html = textile.textile(s)

with open(filename + '.html', 'w') as f:
  f.write(html)

print 'Done: File {s} converted to {s}.html'.format(s=filename)
