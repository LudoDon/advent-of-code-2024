https://adventofcode.com/2024

# Thoughts

### day 01

Part I: decided to sort both lists and then linearly iterate through them.

Part II: instead of adjusting part I, SQL seemed a better fit. So I loaded the data in sqlite (in-memory) en got the result in a single sql query.

### day 02

Part I: iterate through each row, tracking the previous value and previous difference.

Part II: first tried an improvement of part I, thinking I only needed to track the number of decrease/increase-flips and an extra previous difference. But too many exceptional scenario's popped in my head. Switched to brute force: for each row, remove each level and reduce to part I.

### day 03

Part I: just went for a regex with capturing groups. Hadn't done these in python yet, googled to find `re.findall` just returns the capturing groups. Multiplying and summing the result screamed 'map-reduce' to me, and I learned python has `map` and `reduce` out of the box. Nice.

Part II: although a linear scan through the string now seemed the smarter (certainly faster) move, it seemed more interesting to expand on my part I solution: 3 regexes. Now I needed not just the matches, but also their string-index. Googled to find `re.finditer` which returns a so-called `Matching-object` which has `span/start/end`. First started to write a (manual) merge of the three lists of indexes, but resorted to iterating the `mult`-list, getting the maximum of smaller indexes of enable/disable-lists. This feels like O(n^2) and could easily be optimized...but it does the job.

### day 04

Part I: the naive solution: just get all possible lines (horizontal,vertical, diagonal in both directions) and use a regex to find matches in each line. It felt a bit tedious to get the diagonal lines (bookkeeping of indices), and got a flashback to [exercise percolation](https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php) for the Coursera algorithms course.

Part II: feels easier than part I. Pondered to re-use part I by scanning only the diagonal lines and combining them on common 'A's. But the naive solution seemed much easier and faster: walk the grid, for each A just determine its cross en check if the cross-legs are both MAS or SAM.
