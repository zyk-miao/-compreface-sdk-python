from compare_face import CompareFace

compare = CompareFace("http://127.0.0.1", 8000)
rec_service = compare.init_recognition_service('7496cc75-aa24-442c-bf2f-919687d3cfdd')

if __name__ == '__main__':
    # rv = rec_service.add_a_subject('张三')

    # rv = rec_service.rename_a_subject('张三', 'zs')
    # rv = rec_service.delete_a_subject('zs')
    # rv = rec_service.delete_all_subjects()
    # rv = rec_service.get_all_subjects()
    # rv = rec_service.add_a_img('张玉凯', '1.jpg')
    # rv=rec_service.list_all_subjects()
    rv = rec_service.list_saved_img_subject(subject='张玉凯')
    print(rv)
    # rv=rec_service.delete_saved_img_subject()
    # rv = rec_service.delete_a_img('d5e91a1d-c63d-49ca-826b-3e9a4a96c5ae')
    # rv=rec_service.delete_multiple_img(['3d88de1c-4dc4-44da-aacc-eca3ed7b54bb','bfb0130d-c1aa-452a-8d3e-764908e7a3d3'])
    with open('2.jpg', 'wb') as f:
        f.write(rec_service.direct_download_img('2de0cf28-61ce-4381-b588-0a2f4972454e'))
