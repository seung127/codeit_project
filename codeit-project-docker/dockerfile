FROM python:3.11

RUN pip install --no-cache-dir \
    pandas \
    matplotlib \
    pyarrow \
    google-cloud-bigquery \
    google-cloud-storage \
    google-cloud-bigquery-storage \    
    gcsfs \
    db-dtypes \
    jupyterlab


WORKDIR /workspace
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
