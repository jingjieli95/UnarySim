# %%
%load_ext autoreload
%autoreload 2

# %%
import torch
from UnarySim.sw.stream.gen import RawScale

# %%
input = torch.randn([2, 3]).cuda()
print(input)
srcbin = RawScale(input, mode="unipolar", percentile=99).cuda()
print(srcbin)
print(srcbin())


# %%
srcbin2 = RawScale(input, mode="bipolar")
print(srcbin2())

# %%
