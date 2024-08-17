# Solution

The script `main.py` that creates the model also validates that the model contains the correct flag after creation. You can read the `main.py` file to understand how the flag is hidden in the model if you simply want the code.

## Write-up

Let's start by looking at the title and the description of the challenge. The title is "Weight of Secrets" and the description mentions that the flag is hidden in the model.

We have multiple references to the "Weight" of the model, which is a term used in machine learning to refer to the parameters of the model.

The "Cartesian Glide" is also mentioned, which is a reference to another challenge of the CTF.

The tags for that challenge are Steg and AI/ML, which confirms that the flag is hidden in the model.

The file provided is a `.pth` file. A Google search of that extension will tell you that it is a PyTorch model file. PyTorch is a popular library for machine learning.

And finally, the flag format is given and it tells us that the flag is 24 characters long without the `flag-` prefix, we are looking for 29 characters in total then.


**Note:** Pytorch can run on CPU, no GPU is needed for that challenge. 

If we write a simple script to read the model and print it to see what we have:

```python
import torch

# Load the model
torch_model = torch.load("model.pth")

# Print the model to see the structure
print(torch_model)
```

We get the following output:

```bash
Sequential(
  (layer0): Linear(in_features=1, out_features=1, bias=True)
  (layer1): Linear(in_features=1, out_features=1, bias=True)
  (layer2): Linear(in_features=1, out_features=1, bias=True)
  (layer3): Linear(in_features=1, out_features=1, bias=True)
  (layer4): Linear(in_features=1, out_features=1, bias=True)
  (layer5): Linear(in_features=1, out_features=1, bias=True)
  (layer6): Linear(in_features=1, out_features=1, bias=True)
  (layer7): Linear(in_features=1, out_features=1, bias=True)
  (layer8): Linear(in_features=1, out_features=1, bias=True)
  (layer9): Linear(in_features=1, out_features=1, bias=True)
  (layer10): Linear(in_features=1, out_features=1, bias=True)
  (layer11): Linear(in_features=1, out_features=1, bias=True)
  (layer12): Linear(in_features=1, out_features=1, bias=True)
  (layer13): Linear(in_features=1, out_features=1, bias=True)
  (layer14): Linear(in_features=1, out_features=1, bias=True)
  (layer15): Linear(in_features=1, out_features=1, bias=True)
  (layer16): Linear(in_features=1, out_features=1, bias=True)
  (layer17): Linear(in_features=1, out_features=1, bias=True)
  (layer18): Linear(in_features=1, out_features=1, bias=True)
  (layer19): Linear(in_features=1, out_features=1, bias=True)
  (layer20): Linear(in_features=1, out_features=1, bias=True)
  (layer21): Linear(in_features=1, out_features=1, bias=True)
  (layer22): Linear(in_features=1, out_features=1, bias=True)
  (layer23): Linear(in_features=1, out_features=1, bias=True)
  (layer24): Linear(in_features=1, out_features=1, bias=True)
  (layer25): Linear(in_features=1, out_features=1, bias=True)
  (layer26): Linear(in_features=1, out_features=1, bias=True)
  (layer27): Linear(in_features=1, out_features=1, bias=True)
  (layer28): Linear(in_features=1, out_features=1, bias=True)
)
```

We can see that the model is a Sequential model with 29 layers. Each layer is a Linear layer with 1 input feature and 1 output feature.

We are looking for 29 letters, so we can assume that each layer contains a letter of the flag. We also know the starting prefix of the flag, which is `flag-`.

We can write a script to look at the weights of the first five letters and see if we can find the `flag-` prefix in some form:

```python
# Print the parameters of the model
counter = 0
for name, param in torch_model.named_parameters():
    if counter == 5:
        exit(0)

    print(name, param)
    counter += 1
```



The output of the script is:

```bash
layer0.weight Parameter containing:
tensor([[0.1020]], requires_grad=True)
layer0.bias Parameter containing:
tensor([0.5085], requires_grad=True)
layer1.weight Parameter containing:
tensor([[0.1080]], requires_grad=True)
layer1.bias Parameter containing:
tensor([-0.1631], requires_grad=True)
layer2.weight Parameter containing:
tensor([[0.9700]], requires_grad=True)
```

We can see that this script is printing the weight and the bias of the first 3 layers but we are missing the `layer2.bias` parameter. Let's say we were not expecting to see the bias of the layers, we can adapt the script to only print the weights:

```python
# Print the parameters of the model
counter = 0
for name, param in torch_model.named_parameters():
    if counter == 5:
        exit(0)

    if "weight" in name:
        print(name, param)
        counter += 1
```

The output of the script is:

```bash
layer0.weight Parameter containing:
tensor([[0.1020]], requires_grad=True)
layer1.weight Parameter containing:
tensor([[0.1080]], requires_grad=True)
layer2.weight Parameter containing:
tensor([[0.9700]], requires_grad=True)
layer3.weight Parameter containing:
tensor([[0.1030]], requires_grad=True)
layer4.weight Parameter containing:
tensor([[0.4500]], requires_grad=True)
```

We can see the weights here, let's compare to what we are looking for:

| f      | l      | a      | g      | \-     |
| ------ | ------ | ------ | ------ | ------ |
| 0.1020 | 0.1080 | 0.9700 | 0.1030 | 0.4500 |

Now we need to map `f` with `0.1020`, the `l` with `0.1080`... and so on.

At this point, we can search for a few ways to encode a letter with a number. The `0.97` for `a` is a good hint that we are looking at ASCII values.

Now we just need to write a script to decode the weights or simply do it manually since the flag is only 29 characters long. Scripting is a good idea but the float values can be tricky to use since they will need a few rounding to get the correct ASCII value.

**Note** It is also possible to read the weights of a model online with a tool like [Netron](https://netron.app/).

Here is a script that will decode the weights and print the flag:

```python
import torch

# Load the model
torch_model = torch.load("model.pth")

# Automatic solve
flag = ""
for param in torch_model.parameters():

    # Flag is stored in the weights and not in the biases
    if param.data.ndimension() != 2:
        continue
    weight = param.data[0].item()
    # 1. Multiply by 1000 to get the ASCII value
    value = weight * 1000
    # 2. Round the value to the nearest integer
    value = round(value)
    # 3. Convert the integer to ASCII character
    if value < 127:
        value = chr(int(value))
    else:
        # Value is greater than 127 which means it was a letter bellow 100, divide by 10 and convert to ASCII
        value = chr(int(value / 10))
    flag += value

print("Flag:", flag)
