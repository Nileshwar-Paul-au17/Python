'''
There is a Room with capacity M. (maximum M people can be in that room at any instant of time.) There are a total of N people, numbered from 1 to N. All N people are outside the room.

You are given a sequence of Q events of the following form.

+ i : It denotes that the person i (ith person) enters the Room.
− i : It denotes that the person i (ith person) leaves the Room.
Determine whether the sequence of events is Valid or not (i.e. no person leaves the Room before entering and the number of Person in the room does not exceed M at any point of time).


NOTE:
+ i means ith person enters the room(only 1 person enters and that person is the person with id i).
Similarly, - i means ith person leavs the room. At any moment of time , only 1 person is entering/leaving the room.

Input Format

The first line of each test case contains three space-separated integers N,M,Q.
Q lines follow. For each valid j, jth of these lines contains a character ch, followed by a space and an integer i. Here ch is either '+' or '−'.
It is guaranteed that ‘‘+ i" and ‘‘− i" appears at most once for every 1≤i≤N
Constraints

For each test case, print a single line containing one string - "GOOD" if the sequence is Valid, "BAD" otherwise.

Output Format

1 ≤ N≤ 10000
1 ≤ M ≤10000
1 ≤ Q ≤10000
Sample Input 0

2 1 4
+ 1
+ 2
- 1
- 2
Sample Output 0

BAD
Explanation 0

After Person 2 enters the bus, there are two people inside the Room while the capacity of the Room is 1.

Sample Input 1

3 2 3
+ 1
- 2
+ 2
Sample Output 1

BAD
Explanation 1

Person 2 leaves the room before it enters. This is inconsistent

Sample Input 2

3 2 2
+ 1
+ 2
Sample Output 2

GOOD
Contest ends in 30 minutes
Submissions: 23
Max Score: 25
Difficulty: Medium
Rate This Challenge:

    
More
'''
def goodOrBad(N, M, Q, events):
    res = []
    for i in range(Q):
        print (i)
        if events[i][1] == '+':
            res.append(events[i][0])

            if len(res) > M:
                return 'BAD'

        else:
            if events[i][0] in res:

                res.remove(events[i][0])

            else:
                return 'BAD'

    return 'GOOD'


N, M,  Q = map(int, input().split())

events = []

for i in range(Q):
    a = []

    ch, i = (map(str, input().split()))

    a.append(int(i))
    a.append(ch)

    events.append(a)
print(events)
print(goodOrBad(N,M,Q,events))