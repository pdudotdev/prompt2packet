# Manual TCP Prompt Test Suite

## A. Baseline correctness - no clarification (30 tests)

1. send 1 tcp packet to 192.168.56.129 port 80 with SYN flag  
2. send 5 tcp packets to 192.168.56.10 port 22 with RST flag  
3. generate tcp syn packets toward 192.168.56.199 on port 443 count 3  
4. tcp fin packets to 192.168.56.129 port 8080 count 10  
5. send tcp ack packets to 192.168.56.11:25 count 2  
6. send 10 tcp syn ack packets to 192.168.56.129 port 80 seq 1001  
7. send 10 tcp packets to 192.168.56.129 port 80 with SYN flag ttl 66  
8. send 10 tcp packets to 192.168.56.129 port 80 syn window 8193  
9. send 10 tcp packets to 192.168.56.129 port 80 syn ttl 128 window 65535  
10. send 10 tcp packets from 192.168.1.10 to 192.168.56.129 port 80 syn  
11. send 10 tcp packets from 192.168.1.10 port 40000 to 192.168.56.129 port 22 syn  
12. send tcp packets to 192.168.56.129 port 22 with FIN flag count 1  
13. generate tcp rst packets to 192.168.56.129 port 443 count 4  
14. tcp syn packets to 192.168.56.129 port 80 interval 10 count 5  
15. send tcp packets to 192.168.56.129 port 80 syn interval 0 count 3  
16. initiate tcp syn traffic with 3 pkts to 192.168.56.129 on port 21  
17. send tcp ack traffic with 8 packet toward 192.168.56.110 port 110  
18. produce 5 tcp fin packets to 192.168.56.115 port 995  
19. simulate one tcp reset packets against 192.168.56.5 port 8080  
20. generate seven tcp syn packets to 192.168.56.110 port 443  
21. send 5 tcp packets to 192.168.56.129 port 80 with SYN and ACK flags  
22. send 5 tcp packets to 192.168.56.129 port 80 flags syn ack  
23. 9 tcp syn ack packets targeting 192.168.56.129:80  
24. send 5 tcp packets to 192.168.56.129 port 443 with PSH flag  
25. send 5 tcp packets to 192.168.56.129 port 443 with URG flag  
26. generate 5 tcp packets to 192.168.56.129 port 443 flags ece  
27. generate 5 tcp packets to 192.168.56.129 port 443 flags cwr  
28. send 5 tcp packets to 192.168.56.129 port 80 syn ttl 1  
29. send 5 tcp packets to 192.168.56.129 port 80 syn ttl 255  
30. send 5 tcp packets to 192.168.56.129 port 80 syn window 1  

---

## B. Address & port ranges (30 tests)

31. send tcp syn packets from 192.168.77.10-192.168.77.15 to 192.168.56.129 port 80 count 6  
32. send eleven tcp packets to destination range 192.168.56.110-192.168.56.120 port 443 with rst flag  
33. send 6 tcp packets from 192.168.1.10 to 192.168.56.129 port range 8000-8005 syn  
34. send 5 tcp packets from source ip range 192.168.1.1-192.168.1.5 to 192.168.56.129 port range 22-25 syn  
35. send 6 tcp packets from source port range 40000-40005 to 192.168.56.129 port 22 syn  
36. send 3 tcp packets from 192.168.1.10-192.168.1.12 to 192.168.56.129 port range 80-82 syn  
37. send tcp packets to 192.168.56.129-192.168.56.137 port 80 syn count 6  
38. send 3 tcp packets from 192.168.1.10 port 40000-40002 to 192.168.56.129 port 80 syn  
39. send nine tcp packets from 192.168.1.10-192.168.1.15 to destination range 192.168.56.120-192.168.56.128 port 443 ack  
40. send tcp packets to 192.168.56.129 from 192.168.168.168 port range 10000-10010 rst count 5  
41. send 9 tcp packets from source ip range 192.168.1.20-192.168.1.25 to 192.168.56.129 port 80 fin  
42. send 10 tcp packets from 192.168.1.10 to destination range 192.168.56.100-192.168.56.105 port 22 syn  
43. send 3 tcp packets from 192.168.1.10 port 50000 to 192.168.56.129 port range 8080-8082 syn  
44. send 13 tcp packets from source ip range 192.168.1.1-192.168.1.3 to destination range 192.168.56.11-13 port 80 syn  
45. send tcp packets to 192.168.56.129 port 80 syn count 10 using source port range 40000-40005  
46. send 4 tcp packets from source ip range 10.0.0.1-4 to destination 192.168.56.10 port 443  
47. send 50 tcp packets from 10.0.0.1-192.168.56.129 to 192.168.56.10 port range 443-445  
48. generate 11 tcp push packets from 192.168.1.10 port 40000-40010 to 192.168.56.129 port 80  
49. 3 tcp rst packets from source ip range 192.168.0.1-192.168.0.3 to 192.168.56.129 port 22  
50. send 10 tcp ack packets from source range 30000-30005 to destination range 192.168.56.10-192.168.56.12 port 80  

---

## C. Clarification required - 1 round (20 tests)

51. send 5 tcp packets to port 80  
52. send 5 tcp packets to 192.168.56.129  
53. generate tcp traffic with 7 packets to 192.168.56.129 port 443  
54. send 11 tcp packets with syn flag  
55. 22 tcp packets to port 22  
56. generate 3 tcp packets to 192.168.56.10  
57. send 4 tcp packets port 80 syn  
58. send tcp traffic to 192.168.56.129, 5 packets  
59. send 12 tcp packets to port 443  
60. tcp packet to 192.168.56.129 port 22  
61. send one tcp packets to destination 192.168.56.129  
62. send 6 tcp packets with acks  
63. generate 4 tcp packets port 443  
64. 2 tcp packets syn  
65. send tcp traffic to port 25 with 5 packets  
66. send 3 tcp packets to destination range 192.168.56.11-192.168.56.13  
67. send 11 tcp packets from 192.168.1.10  
68. generate tcp traffic using 4 packets to port 80  
69. send 3 tcp packets with both syn and ack flags
70. 5 tcp packets ack and fin and reset

---

## D. Clarification required - 2 rounds (20 tests)

71. send 2 tcp packets  
72. generate tcp traffic, 3 pkts
73. 5 tcp packets  
74. send 4 tcp  
75. generate 6 tcp  
76. send 2 packets  
77. send tcp traffic via 4 packets
78. tcp traffic just one packet 
79. send 12 network packets  
80. generate 3 packets  
81. tcp 3  
82. 9 packets
83. send traffic using 4 packets
84. generate traffic of 3 packets
85. send some packets  
86. tcp fin scan with 5 packets 
87. network test with 4 packets
88. firewall test with just 2 packets
89. packet test, count 5  
90. send 8 test packets  

---

## E. Advanced (10 tests)

91. send 100 tcp syn packets to 192.168.56.129 port 80 ttl 2  
92. send hundred tcp packets to 192.168.56.129 port 80 window 1  
93. send 5 tcp packets to 192.168.56.129 port 80 window 1000000  
94. send 5 tcp packets to 192.168.56.129 port 80 seq 0  
95. send 5 tcp packets to 192.168.56.129 port 80 seq 1000000  
96. send tcp packets to 192.168.56.129 port 80 syn count 100  
97. send 5 tcp packets from 192.168.1.10 to 192.168.56.129 port 80 syn interval 5  
98. send tcp packets from source ip range 192.168.1.1-192.168.1.10 to 192.168.56.129 port 80 syn count 20  
99. send 5 tcp packets from source port range 40000-40020 to 192.168.56.129 port 80 syn  
100. send 5 tcp packets from source ip range 192.168.1.1-192.168.1.5 to destination range 192.168.56.1.1-192.168.56.129 port range 8000-8010 syn  

---

## F. Invalid values (should be rejected or clarified)

101. send 5 tcp packets to 999.999.999.999 port 80 syn  
102. send 5 tcp packets to 10.0.0.256 port 80 syn  
103. send 5 tcp packets to abc.def.ghi.jkl port 80 syn  
104. send 5 tcp packets to 192.168.56.129 port -1 syn  
105. send 5 tcp packets to 192.168.56.129 port 70000 syn  
106. send 5 tcp packets to 192.168.56.129 port 0 syn  
107. send 5 tcp packets to 192.168.56.129 port eighty syn  
108. send 5 tcp packets to 192.168.56.129 port 80 flag FOOBAR  
109. send 5 tcp packets to 192.168.56.129 port 80 flags SYN FAKE  
110. send 5 tcp packets to 192.168.56.129 port 80 flags SYN ACK BAD  
111. send 5 tcp packets to 192.168.56.129 port 80 syn seq -1  
112. send 5 tcp packets to 192.168.56.129 port 80 syn seq abc  
113. send 5 tcp packets to 192.168.56.129 port 80 syn window -10  
114. send 5 tcp packets to 192.168.56.129 port 80 syn window abc  
115. send 5 tcp packets to 192.168.56.129 port 80 syn ttl -1  
116. send -2 tcp packets to 192.168.56.129 port 80 syn ttl 999  
117. send 0 tcp packets to 192.168.56.129 port 80 syn interval -5  
118. send 5 tcp packets to 192.168.56.129 port 80 syn interval abc  
119. send tcp packets to 192.168.56.129 port 80 syn count -1  
120. send tcp packets to 192.168.56.129 port 80 syn count abc  

---

## G. Boundary values (should be accepted or warned)

121. send 5 tcp packets to 192.168.56.129 port 1 syn  
122. send 5 tcp packets to 192.168.56.129 port 65535 syn  
123. send 5 tcp packets to 192.168.56.129 port 80 syn ttl 0  
124. send 5 tcp packets to 192.168.56.129 port 80 syn ttl 1  
125. send 5 tcp packets to 192.168.56.129 port 80 syn ttl 255  
126. send 5 tcp packets to 192.168.56.129 port 80 syn window 0  
127. send 5 tcp packets to 192.168.56.129 port 80 syn window 65535  
128. send 5 tcp packets to 192.168.56.129 port 80 syn seq 0  
129. send 5 tcp packets to 192.168.56.129 port 80 syn seq 4294967295  
130. send 5 tcp packets to 192.168.56.129 port 80 syn interval 0  
131. send 5 tcp packets to 192.168.56.129 port 80 syn interval 10000  
132. send tcp packets to 192.168.56.129 port 80 syn count 1  
133. send tcp packets to 192.168.56.129 port 80 syn count 1000  

---

## H. Invalid or suspicious ranges

134. send 22 tcp packets to 192.168.56.129 port range 65500-65600 syn  
135. send 22 tcp packets to 192.168.56.129 port range -10-20 syn  
136. send 22 tcp packets to 192.168.56.129 port range 100-50 syn  
137. send 22 tcp packets from source port range 70000-70010 to 192.168.56.129 port 80 syn  
138. send 22 tcp packets from source port range abc-def to 192.168.56.129 port 80 syn  
139. send 22 tcp packets to destination range 192.168.56.120-192.168.56.110 port 80 syn  
140. send 22 tcp packets from source ip range 192.168.1.10-999.999.999.999 to 192.168.56.129 port 80 syn  

---

## I. Loopback, broadcast, multicast (source IP)

141. send 4 tcp packets from 127.0.0.1 to 192.168.56.129 port 80 syn  
142. send 4 tcp packets from 0.0.0.0 to 192.168.56.129 port 80 syn  
143. send 4 tcp packets from 255.255.255.255 to 192.168.56.129 port 80 syn  
144. send 4 tcp packets from 224.0.0.1 to 192.168.56.129 port 80 syn  
145. send 4 tcp packets from 239.255.255.250 to 192.168.56.129 port 80 syn  

(Expected: warning or rejection depending on ALLOW_BROADCAST / design)

---

## J. Loopback, broadcast, multicast (destination IP)

146. send 5 tcp packets to 127.0.0.1 port 80 syn  
147. send 5 tcp packets to 0.0.0.0 port 80 syn  
148. send 5 tcp packets to 255.255.255.255 port 80 syn  
149. send 5 tcp packets to 224.0.0.1 port 80 syn  
150. send 5 tcp packets to 239.255.255.250 port 80 syn  

---

## K. Unusual but valid protocol combinations

151. send 6 tcp packets to 192.168.56.129 port 80 flags FIN SYN  
152. send 6 tcp packets to 192.168.56.129 port 80 flags RST ACK  
153. send 6 tcp packets to 192.168.56.129 port 80 flags FIN RST  
154. send 6 tcp packets to 192.168.56.129 port 80 flags SYN FIN ACK  
155. send 6 tcp packets to 192.168.56.129 port 80 flags CWR ECE  

---

## L. Ambiguous or misleading prompts (AI robustness)

156. send 7 secure packets to 192.168.56.129 port 80  
157. send 7 handshake packets to 192.168.56.129 port 80  
158. send 7 connection reset to 192.168.56.129 port 443  
159. simulate 7 connection close to 192.168.56.129 port 22  
160. send 7 suspicious tcp traffic to 192.168.56.129  

(Expected: clarification, not guessing)

---

## M. Mixed valid + invalid fields

161. send 8 tcp packets to 192.168.56.129 port 80 syn ttl -5  
162. send tcp packets to 192.168.56.129 port 70000 syn count 8 
163. send 8 tcp packets from 127.0.0.1 to 999.999.999.999 port 80 syn  
164. send 8 tcp packets to 192.168.56.129 port 80 flags SYN FAKE  
165. send 8 tcp packets to 192.168.56.129 port range 100-200 syn interval -10  

---

## N. Stress / warning scenarios (valid but suspicious)

166. send tcp packets to 192.168.56.129 port 80 syn count 10000  
167. send tcp packets to 192.168.56.129 port 80 syn interval 0 count 1000  
168. send tcp packets from source ip range 192.168.1.1-192.168.1.254 to 192.168.56.129 port 80 syn count 500  
169. send 65536 tcp packets to 192.168.56.129 port range 1-65535 syn  
170. send 3 tcp packets with all flags to 192.168.56.129 port 80  

