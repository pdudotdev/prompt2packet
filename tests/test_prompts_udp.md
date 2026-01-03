# Manual UDP Prompt Test Suite

## A. Baseline correctness – no clarification (15 tests)

1. send 5 udp packets to 192.168.56.129 port 53  
2. send 3 udp packets to 192.168.56.10 port 123  
3. generate 6 udp packets toward 192.168.56.199 on port 161  
4. send 10 udp packets to 192.168.56.129 port 500  
5. send 2 udp packets to 192.168.56.11 port 69  
6. send 7 udp packets to 192.168.56.129 port 1900  
7. send 4 udp packets to 192.168.56.129 port 514  
8. send 5 udp packets to 192.168.56.129 port 137  
9. generate 3 udp packets to 192.168.56.129 port 162  
10. send 8 udp packets to 192.168.56.129 port 1194  
11. send 2 udp packets to 192.168.56.129 port 1812  
12. send 6 udp packets to 192.168.56.115 port 5060  
13. generate 5 udp packets to 192.168.56.129 port 5353  
14. send 3 udp packets to 192.168.56.129 port 11211  
15. send 5 udp packets to 192.168.56.129 port 33434  

---

## B. Address & port ranges (10 tests)

16. send 6 udp packets from 192.168.1.10-192.168.1.15 to 192.168.56.129 port 53  
17. send 5 udp packets to destination range 192.168.56.110-192.168.56.120 port 161  
18. send 6 udp packets from 192.168.1.10 to 192.168.56.129 port range 5000-5005  
19. send 4 udp packets from source ip range 192.168.1.1-192.168.1.5 to 192.168.56.129 port 69  
20. send 6 udp packets from source port range 40000-40005 to 192.168.56.129 port 53  
21. send 3 udp packets to 192.168.56.129-192.168.56.137 port 161  
22. send 5 udp packets from 192.168.1.10 port 40000-40002 to 192.168.56.129 port 123  
23. send 4 udp packets from 192.168.1.10-192.168.1.15 to destination range 192.168.56.120-192.168.56.128 port 500  
24. send 3 udp packets from source ip range 192.168.1.20-192.168.1.25 to 192.168.56.129 port 1900  
25. send 5 udp packets from source port range 30000-30005 to destination range 192.168.56.10-192.168.56.12 port 53  

---

## C. Clarification required – 1 round (10 tests)

26. send 5 udp packets to port 53  
27. send 4 udp packets to 192.168.56.129  
28. generate 6 udp packets to 192.168.56.129  
29. send 7 udp packets  
30. send 3 udp packets to port 69  
31. generate 5 udp packets to destination 192.168.56.10  
32. send 4 udp packets port 123  
33. send udp traffic to 192.168.56.129 with 5 packets  
34. send 6 udp packets to port 161  
35. send 3 udp packets to destination range 192.168.56.11-192.168.56.13  

---

## D. Clarification required – 2 rounds (10 tests)

36. send udp packets  
37. generate udp traffic  
38. udp packets  
39. send udp  
40. generate udp  
41. send packets  
42. send network packets  
43. generate traffic  
44. udp traffic  
45. packet test  

---

## E. Invalid values (should be rejected or clarified)

46. send 5 udp packets to 999.999.999.999 port 53  
47. send 5 udp packets to 10.0.0.256 port 53  
48. send 5 udp packets to abc.def.ghi.jkl port 53  
49. send 5 udp packets to 192.168.56.129 port -1  
50. send 5 udp packets to 192.168.56.129 port 70000  
51. send 5 udp packets to 192.168.56.129 port 0  
52. send 5 udp packets to 192.168.56.129 port fifty  
53. send 5 udp packets to 192.168.56.129 port range 65500-65600  
54. send 5 udp packets to 192.168.56.129 port range 100-50  
55. send 5 udp packets from source port range 70000-70010 to 192.168.56.129 port 53  

---

## F. Loopback, broadcast, multicast IPs

56. send 4 udp packets from 127.0.0.1 to 192.168.56.129 port 53  
57. send 4 udp packets from 0.0.0.0 to 192.168.56.129 port 53  
58. send 4 udp packets from 255.255.255.255 to 192.168.56.129 port 53  
59. send 4 udp packets from 224.0.0.1 to 192.168.56.129 port 53  
60. send 4 udp packets from 239.255.255.250 to 192.168.56.129 port 1900  

61. send 5 udp packets to 127.0.0.1 port 53  
62. send 5 udp packets to 0.0.0.0 port 53  
63. send 5 udp packets to 255.255.255.255 port 53  
64. send 5 udp packets to 224.0.0.1 port 53  
65. send 5 udp packets to 239.255.255.250 port 1900  

(Expected: warning or rejection depending on ALLOW_BROADCAST / design)

---

## G. Stress / warning scenarios (valid but suspicious)

66. send 100 udp packets to 192.168.56.129 port 53  
67. send 500 udp packets to 192.168.56.129 port 123 interval 0  
68. send 300 udp packets from source ip range 192.168.1.1-192.168.1.254 to 192.168.56.129 port 53  
69. send 200 udp packets to 192.168.56.129 port range 1-65535  
70. send 1000 udp packets to 192.168.56.129 port 53  

