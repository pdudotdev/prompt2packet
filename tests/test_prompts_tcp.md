# Manual TCP Prompt Test Suite (100 Tests)

## A. Baseline correctness — no clarification (30 tests)

1. send 1 tcp packet to 10.0.0.5 port 80 with SYN flag  
2. send 5 tcp packets to 192.168.1.10 port 22 with RST flag  
3. generate tcp syn packets toward 10.1.1.1 on port 443 count 3  
4. tcp fin packets to 10.0.0.20 port 8080 count 10  
5. send tcp ack packets to 172.16.0.5 port 25 count 2  
6. send tcp syn ack packets to 10.0.0.5 port 80 seq 1000  
7. send tcp packets to 10.0.0.5 port 80 with SYN flag ttl 64  
8. send tcp packets to 10.0.0.5 port 80 syn window 8192  
9. send tcp packets to 10.0.0.5 port 80 syn ttl 128 window 65535  
10. send tcp packets from 192.168.1.10 to 10.0.0.5 port 80 syn  
11. send tcp packets from 192.168.1.10 port 40000 to 10.0.0.5 port 22 syn  
12. send tcp packets to 10.0.0.5 port 22 with FIN flag count 1  
13. generate tcp rst packets to 10.0.0.5 port 443 count 4  
14. tcp syn packets to 10.0.0.5 port 80 interval 10 count 5  
15. send tcp packets to 10.0.0.5 port 80 syn interval 0 count 3  
16. initiate tcp syn traffic to 10.0.0.5 on port 21  
17. send tcp ack traffic toward 10.0.0.10 port 110  
18. produce tcp fin packets to 10.0.0.15 port 995  
19. simulate tcp reset packets against 192.168.0.5 port 8080  
20. generate 7 tcp syn packets to 10.10.10.10 port 443  
21. send tcp packets to 10.0.0.5 port 80 with SYN and ACK flags  
22. send tcp packets to 10.0.0.5 port 80 flags syn ack  
23. tcp syn ack packets targeting 10.0.0.5:80  
24. send tcp packets to 10.0.0.5 port 443 with PSH flag  
25. send tcp packets to 10.0.0.5 port 443 with URG flag  
26. generate tcp packets to 10.0.0.5 port 443 flags ece  
27. generate tcp packets to 10.0.0.5 port 443 flags cwr  
28. send tcp packets to 10.0.0.5 port 80 syn ttl 1  
29. send tcp packets to 10.0.0.5 port 80 syn ttl 255  
30. send tcp packets to 10.0.0.5 port 80 syn window 1  

---

## B. Address & port ranges (30 tests)

31. send tcp syn packets from 192.168.1.10-192.168.1.15 to 10.0.0.5 port 80 count 6  
32. send tcp packets to destination range 10.0.0.10-10.0.0.20 port 443 with rst flag  
33. send tcp packets from 192.168.1.10 to 10.0.0.5 port range 8000-8005 syn  
34. send tcp packets from source ip range 192.168.1.1-192.168.1.5 to 10.0.0.5 port range 22-25 syn  
35. send tcp packets from source port range 40000-40005 to 10.0.0.5 port 22 syn  
36. send tcp packets from 192.168.1.10-192.168.1.12 to 10.0.0.5 port range 80-82 syn  
37. send tcp packets to 10.0.0.5-10.0.0.7 port 80 syn count 6  
38. send tcp packets from 192.168.1.10 port 40000-40002 to 10.0.0.5 port 80 syn  
39. send tcp packets from 192.168.1.10-192.168.1.15 to destination range 10.0.0.5-10.0.0.8 port 443 ack  
40. send tcp packets to 10.0.0.5 port range 10000-10010 rst count 5  
41. send tcp packets from source ip range 192.168.1.20-192.168.1.25 to 10.0.0.5 port 80 fin  
42. send tcp packets from 192.168.1.10 to destination range 10.0.0.100-10.0.0.105 port 22 syn  
43. send tcp packets from 192.168.1.10 port 50000 to 10.0.0.5 port range 8080-8082 syn  
44. send tcp packets from source ip range 192.168.1.1-192.168.1.3 to destination range 10.0.0.1-10.0.0.3 port 80 syn  
45. send tcp packets to 10.0.0.5 port 80 syn count 10 using source port range 40000-40005  
46. send tcp packets from source ip range 10.0.0.1-10.0.0.4 to destination 192.168.1.10 port 443  
47. send tcp packets from 10.0.0.1-10.0.0.5 to 192.168.1.10 port range 443-445  
48. generate tcp packets from 192.168.1.10 port 40000-40010 to 10.0.0.5 port 80  
49. tcp packets from source ip range 192.168.0.1-192.168.0.3 to 10.0.0.5 port 22  
50. send tcp packets from source port range 30000-30005 to destination range 10.0.0.10-10.0.0.12 port 80  

---

## C. Clarification required — 1 round (20 tests)

51. send tcp packets to port 80  
52. send tcp packets to 10.0.0.5  
53. generate tcp traffic to 10.0.0.5 port 443  
54. send tcp packets with syn flag  
55. tcp packets to port 22  
56. generate tcp packets to 192.168.1.10  
57. send tcp packets port 80 syn  
58. send tcp traffic to 10.0.0.5  
59. send tcp packets to port 443  
60. tcp packets to 10.0.0.5 port 22  
61. send tcp packets to destination 10.0.0.5  
62. send tcp packets with ack  
63. generate tcp packets port 443  
64. tcp packets syn  
65. send tcp traffic to port 25  
66. send tcp packets to destination range 10.0.0.1-10.0.0.3  
67. send tcp packets from 192.168.1.10  
68. generate tcp traffic port 80  
69. send tcp packets syn ack  
70. tcp packets ack  

---

## D. Clarification required — 2 rounds (20 tests)

71. send tcp packets  
72. generate tcp traffic  
73. tcp packets  
74. send tcp  
75. generate tcp  
76. send packets  
77. send tcp traffic  
78. tcp traffic  
79. send network packets  
80. generate packets  
81. tcp  
82. packets  
83. send traffic  
84. generate traffic  
85. send some packets  
86. tcp scan  
87. network test  
88. firewall test  
89. packet test  
90. send test packets  

---

## E. Advanced / edge realism (10 tests)

91. send tcp syn packets to 10.0.0.5 port 80 ttl 2  
92. send tcp packets to 10.0.0.5 port 80 window 1  
93. send tcp packets to 10.0.0.5 port 80 window 1000000  
94. send tcp packets to 10.0.0.5 port 80 seq 0  
95. send tcp packets to 10.0.0.5 port 80 seq 1000000  
96. send tcp packets to 10.0.0.5 port 80 syn count 100  
97. send tcp packets from 192.168.1.10 to 10.0.0.5 port 80 syn interval 5  
98. send tcp packets from source ip range 192.168.1.1-192.168.1.10 to 10.0.0.5 port 80 syn count 20  
99. send tcp packets from source port range 40000-40020 to 10.0.0.5 port 80 syn  
100. send tcp packets from source ip range 192.168.1.1-192.168.1.5 to destination range 10.0.0.1-10.0.0.5 port range 8000-8010 syn  

---

## F. Invalid values (should be rejected or clarified)

1. send tcp packets to 999.999.999.999 port 80 syn  
2. send tcp packets to 10.0.0.256 port 80 syn  
3. send tcp packets to abc.def.ghi.jkl port 80 syn  
4. send tcp packets to 10.0.0.5 port -1 syn  
5. send tcp packets to 10.0.0.5 port 70000 syn  
6. send tcp packets to 10.0.0.5 port 0 syn  
7. send tcp packets to 10.0.0.5 port eighty syn  
8. send tcp packets to 10.0.0.5 port 80 flag FOOBAR  
9. send tcp packets to 10.0.0.5 port 80 flags SYN FAKE  
10. send tcp packets to 10.0.0.5 port 80 flags SYN ACK BAD  
11. send tcp packets to 10.0.0.5 port 80 syn seq -1  
12. send tcp packets to 10.0.0.5 port 80 syn seq abc  
13. send tcp packets to 10.0.0.5 port 80 syn window -10  
14. send tcp packets to 10.0.0.5 port 80 syn window abc  
15. send tcp packets to 10.0.0.5 port 80 syn ttl -1  
16. send tcp packets to 10.0.0.5 port 80 syn ttl 999  
17. send tcp packets to 10.0.0.5 port 80 syn interval -5  
18. send tcp packets to 10.0.0.5 port 80 syn interval abc  
19. send tcp packets to 10.0.0.5 port 80 syn count -1  
20. send tcp packets to 10.0.0.5 port 80 syn count abc  

---

## G. Boundary values (should be accepted or warned)

21. send tcp packets to 10.0.0.5 port 1 syn  
22. send tcp packets to 10.0.0.5 port 65535 syn  
23. send tcp packets to 10.0.0.5 port 80 syn ttl 0  
24. send tcp packets to 10.0.0.5 port 80 syn ttl 1  
25. send tcp packets to 10.0.0.5 port 80 syn ttl 255  
26. send tcp packets to 10.0.0.5 port 80 syn window 0  
27. send tcp packets to 10.0.0.5 port 80 syn window 65535  
28. send tcp packets to 10.0.0.5 port 80 syn seq 0  
29. send tcp packets to 10.0.0.5 port 80 syn seq 4294967295  
30. send tcp packets to 10.0.0.5 port 80 syn interval 0  
31. send tcp packets to 10.0.0.5 port 80 syn interval 10000  
32. send tcp packets to 10.0.0.5 port 80 syn count 1  
33. send tcp packets to 10.0.0.5 port 80 syn count 1000  

---

## H. Invalid or suspicious ranges

34. send tcp packets to 10.0.0.5 port range 65500-65600 syn  
35. send tcp packets to 10.0.0.5 port range -10-20 syn  
36. send tcp packets to 10.0.0.5 port range 100-50 syn  
37. send tcp packets from source port range 70000-70010 to 10.0.0.5 port 80 syn  
38. send tcp packets from source port range abc-def to 10.0.0.5 port 80 syn  
39. send tcp packets to destination range 10.0.0.20-10.0.0.10 port 80 syn  
40. send tcp packets from source ip range 192.168.1.10-999.999.999.999 to 10.0.0.5 port 80 syn  

---

## I. Loopback, broadcast, multicast (source IP)

41. send tcp packets from 127.0.0.1 to 10.0.0.5 port 80 syn  
42. send tcp packets from 0.0.0.0 to 10.0.0.5 port 80 syn  
43. send tcp packets from 255.255.255.255 to 10.0.0.5 port 80 syn  
44. send tcp packets from 224.0.0.1 to 10.0.0.5 port 80 syn  
45. send tcp packets from 239.255.255.250 to 10.0.0.5 port 80 syn  

(Expected: warning or rejection depending on ALLOW_BROADCAST / design)

---

## J. Loopback, broadcast, multicast (destination IP)

46. send tcp packets to 127.0.0.1 port 80 syn  
47. send tcp packets to 0.0.0.0 port 80 syn  
48. send tcp packets to 255.255.255.255 port 80 syn  
49. send tcp packets to 224.0.0.1 port 80 syn  
50. send tcp packets to 239.255.255.250 port 80 syn  

---

## K. Unusual but valid protocol combinations

51. send tcp packets to 10.0.0.5 port 80 flags FIN SYN  
52. send tcp packets to 10.0.0.5 port 80 flags RST ACK  
53. send tcp packets to 10.0.0.5 port 80 flags FIN RST  
54. send tcp packets to 10.0.0.5 port 80 flags SYN FIN ACK  
55. send tcp packets to 10.0.0.5 port 80 flags CWR ECE  

---

## L. Ambiguous or misleading prompts (AI robustness)

56. send secure packets to 10.0.0.5 port 80  
57. send handshake packets to 10.0.0.5 port 80  
58. send connection reset to 10.0.0.5 port 443  
59. simulate connection close to 10.0.0.5 port 22  
60. send suspicious tcp traffic to 10.0.0.5  

(Expected: clarification, not guessing)

---

## M. Mixed valid + invalid fields

61. send tcp packets to 10.0.0.5 port 80 syn ttl -5  
62. send tcp packets to 10.0.0.5 port 70000 syn count 5  
63. send tcp packets from 127.0.0.1 to 999.999.999.999 port 80 syn  
64. send tcp packets to 10.0.0.5 port 80 flags SYN FAKE  
65. send tcp packets to 10.0.0.5 port range 100-200 syn interval -10  

---

## N. Stress / warning scenarios (valid but suspicious)

66. send tcp packets to 10.0.0.5 port 80 syn count 10000  
67. send tcp packets to 10.0.0.5 port 80 syn interval 0 count 1000  
68. send tcp packets from source ip range 192.168.1.1-192.168.1.254 to 10.0.0.5 port 80 syn count 500  
69. send tcp packets to 10.0.0.5 port range 1-65535 syn  
70. send tcp packets with all flags to 10.0.0.5 port 80  

