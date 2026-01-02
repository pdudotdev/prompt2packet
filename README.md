# prompt2packet
AI-assisted network traffic generator written in Python. Transforms user prompt into packets being sent on the wire. Useful for QA testing, pentesting, or educational purposes.

## End-to-End Flow Example

This section explains **exactly what prompt2packet does** when a user enters a prompt, let's say:

`send 10 tcp syn packets to port 9999`

This walkthrough lists **each step in order**, **which module is involved**, and **why it is called**.

### 🔸 1. Application entry point - p2p.py

**Purpose of this module:**  
p2p.py is the orchestrator. It coordinates the entire application.

What happens:
- The banner remembers the user what tool they are running
- Root privileges are checked
- CLI arguments are parsed (e.g. --test)
- The user is prompted for input

The raw user input string is captured:

`send 10 tcp syn packets to port 9999`

p2p.py then passes this string to the AI interpreter.

### 🔸 2. Natural language parsing - ai/interpreter.py

**Purpose of this module:**  
To translate human language into structured data without guessing.

What happens:
- The AI receives the user text
- It produces a best-effort JSON object
- Required fields that are not explicitly mentioned are omitted

Typical AI output:
```
{
  "protocol": "tcp",
  "count": 10,
  "dst_port": 9999,
  "flags": ["SYN"]
}
```
This JSON is returned to p2p.py.

**Keep in mind!** No validation happens here.

### 🔸 3. Protocol dispatch - p2p.py & registry.py

**Purpose of this step:**  
To determine which schema applies in this case.

What happens:
- p2p.py reads `intent_data["protocol"]`
- Using **registry.py**, it maps `tcp` -> TCPIntent schema
- The application now knows which schema defines correctness

### 🔸 4. Schema validation (first pass) - schemas/tcp.py

**Purpose of this module:**  
Schemas define what fields are mandatory and which are optional.

For the **TCPIntent** schema, required fields include:
- protocol
- dst_ip
- dst_port
- flags

At this point, `dst_ip` is missing.

Pydantic raises a *ValidationError* indicating missing required fields.

### 🔸 5. Clarification loop - p2p.py

**Let's clarify the clarification step:**  
Missing information should be requested, **not** guessed.

What happens:
- p2p.py inspects the ValidationError
- It extracts missing required fields (in this case, `dst_ip`)
- It asks the AI engine to ask a polite clarification question

User sees something like:

`Please provide the destination IP address.`

Execution pauses until the user responds.

### 🔸 6. User clarification → AI again - ai/interpreter.py

User replies:

`192.168.56.129`

The AI converts this response into structured JSON:
```
{
  "dst_ip": "192.168.56.129"
}
```
Then, p2p.py merges this into the existing intent data.

### 🔸 7. Schema validation (second pass) - schemas/tcp.py

**Why validation runs again:**  
Every clarification response must still be validated.

Now all required fields are present:
- protocol
- dst_ip
- dst_port
- flags

Validation succeeds.

### 🔸 8. Semantic validation - validation/rules.py

**Purpose of this module:**  
Some rules cannot be expressed in schemas alone.

Examples:
- Packet count limits

In this case:
- count = 10

No semantic violations occur. Good, let's move on.

### 🔸 9. Execution planning - planner/execution.py

**Purpose of this module:**  
To separate intent from execution mechanics.

A deterministic execution plan is built containing:
- protocol
- packet template
- count
- interval

Example plan structure:
```
{
  "protocol": "tcp",
  "template": {
    "dst_ip": "192.168.56.129",
    "dst_port": 9999,
    "flags": ["SYN"],
    "src_port": "random"
  },
  "count": 10,
  "interval_ms": 0
}
```
### 🔸 10. Packet sending loop - sender/transmit.py

**Purpose of this module:**  
To control execution and iteration.

What happens:
- The correct packet builder is selected via **registry.py**
- A loop runs `count` times (10, here)
- For each iteration, a packet is built and sent (or printed in test mode)

### 🔸 11. Packet construction - packet/tcp.py

**Purpose of this module:**  
To convert intent fields into real packets.

For each packet:
- IP header is constructed
- Destination IP is applied
- Source port is selected
- TCP flags are mapped (`SYN` to `S`)
- A complete TCP packet is returned

This module just assembles the packet.

### 🔸 12. Wire execution - sender/transmit.py

**Purpose:**
To place the packet on the wire (or display it).

Depending on mode:
- **LIVE** mode: packets are sent with Scapy
- **TEST** mode: a packet summary is printed

The sender keeps track of how many packets were processed.

### 🔸 13. Result summary - observe/explain.py

**Purpose of this module:**  
To give clear human feedback.

Example output:
```
Execution summary:
- Protocol: TCP
- Packets sent: 10
- Mode: LIVE
```
