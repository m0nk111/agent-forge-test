# Agent-Forge Test Repository 🧪

This is a **dedicated test repository** for the Agent-Forge multi-agent system.

## Purpose

Safe environment for testing Agent-Forge functionality without affecting production repositories:

- ✅ Test issue claiming and processing
- ✅ Test code generation and PR creation
- ✅ Test PR reviews and auto-merge
- ✅ Validate new features before production deployment
- ✅ E2E validation of agent workflows

## Status

- **Environment**: Test
- **Auto-Merge**: ✅ Enabled (safe in test)
- **Bot Accounts**: m0nk111-post, m0nk111-qwen-agent, m0nk111-coder1
- **Claim Timeout**: 60 minutes
- **Max Concurrent Issues**: 2

## Usage

### Running in Test Mode

```bash
# Set environment variable
export AGENT_FORGE_ENV=test

# Run polling service
python engine/runners/polling_service.py

# Or one-liner
AGENT_FORGE_ENV=test python engine/runners/polling_service.py
```

### Creating Test Issues

Test issues should be labeled with `agent-ready` for automatic pickup:

```markdown
## Example Test Issue

Title: 🧪 TEST: [Description of task]

Labels: agent-ready, test
```

## Repository Rules

- **Production Code**: Never commit production code here
- **Test Only**: All commits should be marked as test
- **Auto-Merge**: PRs are auto-merged if approved (safe in test env)
- **Cleanup**: Repository may be periodically cleaned

## Environment Validation

The polling service automatically validates:
- ✅ Test-only repos cannot be accessed in production mode
- ✅ Production-only repos cannot be accessed in test mode
- ✅ Repository access is environment-appropriate

## Links

- **Production Repo**: [agent-forge](https://github.com/m0nk111/agent-forge)
- **Documentation**: See production repo docs/
- **Issues**: Use this repo for testing, production repo for real issues

---

**⚠️ This is a test repository - Do not use for production code!**
