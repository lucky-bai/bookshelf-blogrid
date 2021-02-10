import csv

TEMPLATE = """
<!-- wp:html -->
<center>ILINK</center>
<!-- /wp:html -->

<!-- wp:paragraph -->
REVIEW
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center"} -->
<p class="has-text-align-center"><a href="TLINK" target="_blank" rel="noreferrer noopener">View Book on Amazon.com</a></p>
<!-- /wp:paragraph -->
"""

csvr = csv.reader(open('amazon-links.csv', 'r'))
next(csvr)
for row in csvr:
  print(row[0])

  tlink = row[1]
  ilink = row[2]

  # Add a target=_blank in image link
  ilink = ilink.replace('a href', 'a target="_blank" href')

  output = TEMPLATE.replace('ILINK', ilink).replace('TLINK', tlink)
  print(output)
