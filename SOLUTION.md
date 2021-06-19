To solve this problem, I went with the first idea in my head, which was to iterate
through the data to classify everything. The method to categorize the "funniness"
I used was to simply count how many times a particular sales rep said something funny
in a conversation. My code does this  by looping over all of the sentences. It keeps
a running tally of funny things said by sales reps respective to users and then
attributes them to the correct user. The result is saved and then sorted.

I do realize that this approach wouldn't be very feasible for larger datasets, as
my previous approach of looping through everything isn't optimal for speed and
would take a while. Expanding on this feature would require a different approach,
such as possibly sorting the data first to clean it up, and then assigning values
to sentences and/or conversations. The method I used to rank funniness could also
be tweaked to be more specific to if a customer responded positively to something
funny that was said, which might provide a more accurate result. There seemed to
be many different ways to rank them.
