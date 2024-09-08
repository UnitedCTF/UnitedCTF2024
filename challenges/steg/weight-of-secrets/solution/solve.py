import torch


# Load the model
torch_model = torch.load("model.pth")

# Print the model to see the structure
print(torch_model)

# Print the parameters of the model
counter = 0
for name, param in torch_model.named_parameters():
    if counter == 5:
        break

    if "weight" in name:
        print(param[0][0].item())
        counter += 1

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
