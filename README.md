# uOttaJudge

**uOttaJudge** is a powerful project expo judging system tailored for uOttaHack hackathon and other events; It provides a reliable and efficient platform for evaluating projects showcased.

## Design

uOttaJudge operates on the principle of pairwise comparisons, offering a distinctive approach to project evaluation.

## Status

uOttaJudge is currently a stable software solution; however, it's essential to thoroughly test and understand the system before integrating it into your event. Deploy the system in advance, explore its features, and refer to the provided documentation for guidance.

## Deployment

Deploying uOttaJudge is straightforward. The latest stable version is available in the `master` branch of the repository. Ensure you have Python 3, Flask, NumPy, SciPy, and PostgreSQL installed. Utilize the provided Heroku deployment button or set up the application manually on your server. Refer to the detailed deployment instructions in the [README](https://github.com/qerope/uottajudge/blob/master/README.md).

## Configuration

Customize uOttaJudge to fit your event's requirements by configuring settings in the `config.yaml` file or through environment variables. Detailed instructions are provided in the configuration template file (`config.template.yaml`). Customize settings such as email configuration, database setup, and more to tailor uOttaJudge to your needs.

## Troubleshooting

Encountering issues? Refer to the [troubleshooting guide](https://github.com/qerope/uottajudge/wiki/Troubleshooting) in the uOttaJudge wiki for assistance. Common issues and solutions are documented to help you resolve any deployment or usage challenges efficiently.

## Use

Administer uOttaJudge through the intuitive admin interface accessible at `/admin`. Log in using the default credentials (`admin` username and your chosen password) to manage projects, judges, and the judging process. The system automates judging and ranking, simplifying the overall process for both organizers and participants.

## Development

Interested in contributing to uOttaJudge? Excellent! Refer to the [DEVELOPMENT.md](https://github.com/qerope/uottajudge/blob/master/DEVELOPMENT.md) file for a comprehensive guide on setting up a development environment. Whether you're fixing bugs, adding features, or improving documentation, your contributions are valued and appreciated.

