# #!/bin/bash

# # Check if CUDA is available in PyTorch
# python -c "import torch; print('CUDA available' if torch.cuda.is_available() else 'CUDA not available') " || true

# # Run the server module
# python -m server || true

# # python -m uvicorn server:app --host 0.0.0.0
# # gunicorn -w 4 -k uvicorn.workers.UvicornWorker server:app 