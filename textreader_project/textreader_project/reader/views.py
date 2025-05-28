import os
from django.conf import settings
from django.shortcuts import render
from .forms import UploadTextForm
from .mongo_utils import get_database  # ✅ Import this


def upload_file(request):
    content = ''
    form = UploadTextForm()

    if request.method == 'POST' and request.FILES.get('file'):
        form = UploadTextForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']

            # Ensure MEDIA_ROOT directory exists
            media_dir = settings.MEDIA_ROOT
            os.makedirs(media_dir, exist_ok=True)

            # Save file to media directory
            file_path = os.path.join(media_dir, uploaded_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Try reading the uploaded file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # ✅ Insert into MongoDB after reading
                db = get_database()
                db['uploaded_files'].insert_one({
                    "filename": uploaded_file.name,
                    "content": content,
                })

            except Exception as e:
                content = f"Error reading file: {e}"

    return render(request, 'upload.html', {
        'form': form,
        'content': content
    })
