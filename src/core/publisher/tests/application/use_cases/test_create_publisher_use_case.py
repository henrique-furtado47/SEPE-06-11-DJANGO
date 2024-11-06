from unittest.mock import create_autospec
from src.core.publisher.domain.interfaces import PublisherRepository
from src.core.publisher.application.use_cases.create_publisher import CreatePublisherUseCase, CreatePublisherInput, CreatePublisherOutput

#AAA - Arrange - Act - Assert
class TestCreatePublisherUseCase:
    def test_create_valid_publisher(self):
        mock_repository = create_autospec(PublisherRepository)
        use_case= CreatePublisherUseCase(repository=mock_repository)
        request = CreatePublisherInput(
            name="Test Publisher", 
            description="Test Description")
        response= use_case.execute(request)
        assert response.id is not None
        assert mock_repository.create.called
        assert isinstance(response, CreatePublisherOutput)