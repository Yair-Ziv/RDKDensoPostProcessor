# RoboDK Post Processor for Denso VM-60B1 (Y.A.I.R)

![Denso VM-60B1](https://www.denso-wave.com/imageupd/21002/14160_contents4.png)

## Description

Welcome to Y.A.I.R - Your Automated Industrial Robot! This repository contains a custom post processor for the RoboDK software that is specifically tailored to work with the Denso VM-60B1 robot. The post processor generates a sequence, reference frames, and reference tools in a format that can be easily used to deserialize into a physical sequence for the Denso VM-60B1 robot.

## Prerequisites

Before using the post processor, ensure you have the following:

1. [RoboDK Software](https://robodk.com/): The post processor is designed to work with RoboDK, a powerful robot simulation and offline programming tool.

2. Denso VM-60B1 Robot: This post processor is specifically created for the Denso VM-60B1 robot. Ensure you have access to the robot and its specifications.

## Installation

To use the post processor, follow these steps:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/robodk-post-processor.git
```

2. Open RoboDK and go to `File > Load Application`.

3. Select the `robodk-post-processor.py` file from the cloned repository.

4. The post processor will now be loaded into RoboDK.

## Usage

Follow these instructions to use the post processor with the Denso VM-60B1 robot:

1. Design your robot program in RoboDK with all the necessary waypoints and movements.

2. Go to `File > Save Program As` and choose "Denso VM-60B1" as the target post processor.

3. Provide the desired file name and save the program.

4. The post processor will generate a sequence of instructions, reference frames, and reference tools specific to the Denso VM-60B1 robot.

5. You can now transfer the generated sequence to the physical Denso VM-60B1 robot for execution.


## Disclaimer

**USE AT YOUR OWN RISK:** The post processor is provided as-is and might not cover all possible edge cases or scenarios. Double-check the generated sequence and perform thorough testing before using it on the physical robot. The creators and contributors of this repository are not responsible for any potential damage or errors caused by the usage of this post processor.

## Contributing

We welcome contributions to this repository! If you find any issues, have suggestions for improvements, or want to add support for more robot models, please open an issue or submit a pull request.

## Contact

If you have any questions or need further assistance, feel free to contact us at:

- Email: your-email@example.com
- GitHub: [YourUsername](https://github.com/your-username)

Happy Robot Programming with Y.A.I.R - Your Automated Industrial Robot!
