from ipykernel.kernelapp import IPKernelApp
from .kernel import GradleKernel
IPKernelApp.launch_instance(kernel_class=GradleKernel)
