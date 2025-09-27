# AnonyposRAT — Educational Simulation (LOCAL only)

> **IMPORTANT — READ FIRST**
>
> This repository is an **educational simulation** intended to teach basic TCP sockets, console interfaces, and client/server structure in Python. **Do not** use this code to control, spy on, or damage computers you do not own or have explicit permission to test. Run this project only on machines you control or inside an isolated lab environment (virtual machines, isolated networks). Unauthorized use is illegal.

---

## Project Purpose

AnonyposRAT (simulation) demonstrates:

* Basic usage of Python TCP sockets (bind, listen, accept, send/receive)
* A minimal console command loop for interacting with a single connection
* Patterns for building simple client/server interactions and message loops

**All potentially invasive features (screenshots, camera access, remote command execution, file deletion) are disabled or replaced by safe simulations.** This repository is explicitly for **education and research in controlled, lawful environments**.

---

## Quick Start (Local Simulation)

1. Clone the repository:

```bash
git clone https://github.com/anonypos-dz/AnonyposRAT.git
cd AnonyposRAT
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # if a requirements file exists
```

3. Inspect the code and confirm you understand the behavior before running.

4. Start the server (server is configured to default to `127.0.0.1` / `0.0.0.0` depending on config; prefer `127.0.0.1` for local labs):

```bash
python3 server.py
```

---

## Commands & Options (What each command does — **simulation mode**)

> **Note:** Each command below is described as it exists in the educational simulation. Commands that would normally be intrusive are implemented as **no-op** or return **fake/simulated results**.

### Global / Offline menu commands (entered at the main prompt `AnonyposRAT>>`)

* `help`
  Displays a short helper listing for the offline menu. (Simulation: prints offline command helper.)

* `clear`
  Clears the console screen.

* `set host <host>`
  Update the stored host value in memory. In simulation this only changes an in-memory setting and does not validate external hosts. Use this to learn how configuration is passed to server code.

* `set port <port>`
  Update the stored port value in memory. Input is validated to be numeric and reasonably small (simulation). Does not bind sockets until `listen` is used.

* `settings`
  Show current configuration (Host and Port). Useful to understand how variables are used before binding sockets.

* `listen`
  Start the server listener. The server will create a TCP socket, call `setsockopt(SO_REUSEADDR, 1)`, `bind()`, `listen()` and `accept()` a single incoming test connection. **Run this only on `127.0.0.1` or in an isolated lab.**

* `exit`
  Exit the offline menu/program. In the simulation the process will terminate gracefully.

---

### Server interactive prompt (after a connection is accepted)

When a client connects, the server switches to a connected prompt like: `AnonyposRAT@<client-ip>~$`

* `exit`
  Close the listening socket and return to the offline menu (or quit the program, depending on how the simulation is configured).

* `clear`
  Clear the server console output.

* `kill`
  Send a `kill` command to the connected client **in the simulation only** (the client will simulate closing). In a real-world tool this would forcibly terminate a remote agent — in this educational repo the action is simulated and no real harm is done.

* `help`
  Show the connected-mode help listing.

* `apps`
  Placeholder: prints `Coming soon!` in the simulation. Intended to illustrate how a server could request a list of installed applications from a client.

* `run <app_name>`
  Placeholder for instructing a remote agent to start an application. In simulation this returns a simulated acknowledgement or a placeholder message.

* `shell <command>`
  In the simulation, this sends a shell request to the connected test client which then returns a **simulated** command output. **Important:** no actual remote shell is created; this demonstrates the messaging pattern only.

* `msger`
  Enter a message mode for interactive message exchange. Type `exit` to leave message mode. Special message `logo` may send a simulated ASCII logo to the client.

---

### Commands referenced in help text but disabled/simulated

The original project included strings mentioning advanced actions. In this educational repository these are explicitly disabled or replaced with simulated responses.

* `screenshot` — **SIMULATED**: returns a placeholder message indicating a screenshot would be taken in a real tool. Does not access any camera or capture screen.
* `sysinfo` — **SIMULATED**: returns fake or sanitized system information for demonstration only.
* `cam_list`, `take_pic <cam_id>`, `take_vid <cam_id> <sec>` — **DISABLED**: camera access is not implemented. These commands are kept only as examples of how command names are designed; they perform no camera operations.
* `fuck_it` (or similarly destructive commands) — **REMOVED / DISABLED**: any destructive operations (file deletion, system sabotage) are removed from the codebase. The repository does not include any code that would destroy data or otherwise harm a machine.

---

## Architecture overview (educational)

* `offline()` (main menu): a loop that accepts configuration commands and controls high-level program state.
* `settings()` : shows the stored `server_host` and `server_port`. Helps students learn how values are passed to the socket layer.
* `server()` : demonstrates socket lifecycle:

  1. `socket.socket(AF_INET, SOCK_STREAM)`
  2. `setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)`
  3. `bind((server_host, server_port))`
  4. `listen(1)` and `accept()`
  5. A loop reading user input and sending commands to the connected (simulated) client.
* Messaging loop patterns show `encode()` / `decode()` usage and a simple framing approach.

---

## Security & Ethics (must read)

* This repository is for **learning only**. Do not deploy it on public networks or against machines you do not own.
* Test inside an isolated lab (VMs, isolated subnets). Take VM snapshots and logs before and after tests.
* Prefer legal learning platforms (TryHackMe, Hack The Box) for practice on real challenges.
* Keep audit logs and explicit, written permissions for any real-world testing.

---

## Suggested safe modifications for learning

* Replace any real I/O with deterministic simulation results so behavior is repeatable for unit tests.
* Add a `--localhost-only` flag that enforces binding to `127.0.0.1` and refuses non-loopback addresses.
* Ad
