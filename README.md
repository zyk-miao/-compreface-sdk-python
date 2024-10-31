# compreface-sdk-python

https://github.com/exadel-inc/CompreFace  Python SDK

# Installation

It can be installed through pip:

```shell
pip install compreface-sdk-python
```

## Initialization
you need the Compreface application. For more details, please refer to https://github.com/exadel-inc/CompreFace.
Then you need to create some service API key from your application
```python
from core.compare_face import CompareFace
from services import RecognitionService, DetectionService, VerificationService

DOMAIN: str = 'http://127.0.0.1'
PORT: int = 8000
API_KEY: str = 'your_face_recognition_key'

compare: CompareFace = CompareFace("DOMAIN", PORT)
rec_service: RecognitionService = compare.init_recognition_service('your_face_recognition_service_key')
detect_service: DetectionService = compare.init_detect_service('your_detection_service_key')
verify_service: VerificationService = compare.init_verify_service('your_verification_service_key')

# some example

# Add a Subject
rec_service.add_a_subject("subject_name")
# Rename a Subject
rec_service.rename_a_subject('subject_name', 'new_subject_name')
# Delete a Subject
rec_service.delete_a_subject('subject_name')
# Delete All Subjects
rec_service.delete_all_subjects()
# List Subjects
rv = rec_service.list_all_subjects()
# Add an Example of a Subject
rec_service.add_a_img('subject_name', 'img_path')
# Recognize Faces from a Given Image
rec_service.recognize('img_path')
# List of All Saved Examples of the Subject
rec_service.list_saved_img_subject()
# or 
rec_service.list_saved_img_subject(subject='subject_name')
# Delete All Examples of the Subject by Name
rec_service.delete_saved_img_by_subject('subject_name')
# Delete an Example of the Subject by ID
rec_service.delete_a_img('img_id')
# Delete Multiple Examples
rec_service.delete_multiple_img(['img_id1','img_id2'])
```
