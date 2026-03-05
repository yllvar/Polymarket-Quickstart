# Contributing to Polymarket Python Integration

Thank you for your interest in contributing to this project! This guide will help you get started with contributing to the Polymarket Python integration.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of prediction markets and blockchain concepts
- Familiarity with Polymarket platform (helpful but not required)

### Development Setup

1. **Fork the Repository**
   ```bash
   # Fork the repository on GitHub, then clone your fork
   git clone https://github.com/yourusername/polymarket-python.git
   cd polymarket-python
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   # Install development dependencies
   pip install -r requirements.txt
   
   # Install additional development tools
   pip install pytest black flake8 mypy pre-commit
   ```

4. **Set Up Pre-commit Hooks**
   ```bash
   pre-commit install
   ```

5. **Configure Environment**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env with your test credentials (NEVER commit real credentials)
   # Use mock credentials for development and testing
   ```

## 📝 Development Guidelines

### Code Style

We follow **PEP 8** style guidelines with some additional conventions:

```bash
# Format code with black
black .

# Check linting with flake8
flake8 .

# Type checking with mypy
mypy .
```

### Code Structure

```
polymarket-python/
├── polymarket_client.py      # Main client module
├── poly-integrate.ipynb      # Educational notebook
├── tests/                    # Test suite
├── docs/                     # Documentation
├── examples/                 # Example scripts
└── utils/                    # Utility functions
```

### Naming Conventions

- **Classes**: `PascalCase` (e.g., `PolymarketClient`)
- **Functions/Variables**: `snake_case` (e.g., `get_market_prices`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `DEFAULT_TIMEOUT`)
- **Private methods**: Leading underscore (e.g., `_setup_client`)

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=polymarket_client

# Run specific test file
pytest tests/test_client.py

# Run tests with verbose output
pytest -v
```

### Writing Tests

1. **Test Structure**: Follow the Arrange-Act-Assert pattern
2. **Mocking**: Use mocks for external API calls
3. **Fixtures**: Use pytest fixtures for common setup
4. **Coverage**: Aim for >80% code coverage

Example test:

```python
import pytest
from unittest.mock import Mock, patch
from polymarket_client import PolymarketClient

class TestPolymarketClient:
    @pytest.fixture
    def client(self):
        return PolymarketClient(use_mock_trading=True)
    
    def test_get_markets_success(self, client):
        """Test successful market retrieval"""
        markets = client.get_markets(limit=5)
        assert 'markets' in markets
        assert isinstance(markets['markets'], list)
    
    @patch('requests.get')
    def test_get_markets_api_error(self, mock_get, client):
        """Test handling of API errors"""
        mock_get.side_effect = requests.RequestException("API Error")
        markets = client.get_markets()
        assert markets == {'markets': []}
```

## 📚 Documentation

### Code Documentation

- Use **docstrings** for all public functions and classes
- Follow **Google style** docstrings
- Include type hints for all function parameters and return values

Example:

```python
def get_market_prices(self, market_id: str) -> Dict[str, float]:
    """Get current prices for a market's outcomes.
    
    Args:
        market_id: The market ID to query
        
    Returns:
        Dictionary mapping outcome names to their current prices
        
    Raises:
        ValueError: If market_id is invalid
        APIError: If the API request fails
    """
    pass
```

### README Updates

When adding new features:
1. Update the features section in README.md
2. Add usage examples
3. Update installation requirements if needed
4. Update API documentation

## 🐛 Bug Reports

### Reporting Bugs

1. **Search existing issues** first to avoid duplicates
2. **Use the bug report template** when creating new issues
3. **Provide detailed information**:
   - Python version
   - Operating system
   - Package versions
   - Error messages and tracebacks
   - Steps to reproduce
   - Expected vs actual behavior

### Bug Fix Process

1. **Create issue** describing the bug
2. **Create branch** from main: `git checkout -b fix/issue-number-description`
3. **Write tests** that reproduce the bug
4. **Fix the bug** while ensuring tests pass
5. **Update documentation** if needed
6. **Submit pull request** with detailed description

## ✨ Feature Requests

### Proposing Features

1. **Check existing issues** for similar requests
2. **Create issue** with "feature request" label
3. **Describe the use case** and why it's valuable
4. **Consider implementation complexity** and trade-offs

### Feature Development

1. **Get approval** from maintainers before starting
2. **Create feature branch**: `git checkout -b feature/feature-name`
3. **Implement with tests**
4. **Update documentation**
5. **Submit pull request**

## 🔄 Pull Request Process

### Before Submitting

1. **Run tests**: Ensure all tests pass
2. **Check code style**: Run black and flake8
3. **Update documentation**: Include relevant changes
4. **Test manually**: Verify functionality works as expected
5. **Rebase**: Keep commit history clean

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added new tests for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No sensitive data committed
```

### Review Process

1. **Automated checks**: CI/CD pipeline runs tests and style checks
2. **Code review**: Maintainers review for quality and correctness
3. **Testing**: Changes tested in different environments
4. **Approval**: At least one maintainer approval required
5. **Merge**: Squash and merge to main branch

## 🔒 Security Considerations

### Never Commit

- **API keys** or **API secrets**
- **Private keys** or **wallet credentials**
- **Personal information** or **sensitive data**
- **Real trading credentials** (use test/mock credentials)

### Security Best Practices

1. **Use environment variables** for all sensitive data
2. **Validate inputs** in all public functions
3. **Handle errors gracefully** without exposing sensitive information
4. **Use HTTPS** for all API communications
5. **Follow principle of least privilege**

## 📦 Release Process

### Version Management

We follow **Semantic Versioning** (SemVer):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Steps

1. **Update version** in `__init__.py` or `setup.py`
2. **Update CHANGELOG.md** with release notes
3. **Create release tag**: `git tag v1.2.3`
4. **Push tag**: `git push origin v1.2.3`
5. **Create GitHub release** with detailed notes

## 🤝 Community Guidelines

### Code of Conduct

1. **Be respectful** and inclusive
2. **Welcome newcomers** and help them learn
3. **Focus on constructive feedback**
4. **Assume good intentions**
5. **Follow GitHub's Community Guidelines**

### Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: For questions and general discussion
- **Discord**: For real-time chat (if available)
- **Email**: For security concerns or private matters

## 🏆 Recognition

### Contributors

All contributors are recognized in:
- **README.md**: Contributors section
- **Release notes**: Acknowledgment of contributions
- **GitHub**: Automatic contributor statistics

### Types of Contributions

We value all types of contributions:
- **Code**: New features, bug fixes, improvements
- **Documentation**: Guides, examples, README updates
- **Testing**: Test cases, bug reports, quality assurance
- **Design**: UI/UX improvements, visualizations
- **Community**: Support, discussions, feedback

## 📞 Contact

### Maintainers

- **Primary Maintainer**: [Your Name](mailto:your.email@example.com)
- **Backup Maintainer**: [Backup Name](mailto:backup.email@example.com)

### Communication Channels

- **GitHub Issues**: For bugs and features
- **GitHub Discussions**: For questions and ideas
- **Email**: For private or security-related matters

---

Thank you for contributing to the Polymarket Python integration project! Your contributions help make prediction markets more accessible to everyone. 🎯
