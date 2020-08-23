
#if entry not entirely capitals and entry not entirely lowers
#   split by space
#   split by cap
#   split by pre-cap
#   careful of numbers...
#else
#   forever:
#       find largest 3+ letter word in entry
#       if found
#           put word into list and remove from entry
#           try again
#       else
#           break
#with list of words
#for word in words
#   for entry in db
#       if word in entry
#           if word not in newdb
#               add word to newdb
#           add entry to list of words