# Evasion Rate!
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
#
# # You can find original data via this link
# # https://docs.google.com/spreadsheets/d/1yokW4aEtWPes63nmtwvU5VOUYUcP9yBq8hFR97Tmo2c/edit?usp=sharing
# data = {
#     "Vulnerability": [
#         "regex_dos", "empty-aes-key", "insufficient-dsa-key-size",
#         "disabled-cert-validation", "direct-use-of-jinja2", "avoid-pickle",
#         "request-with-http", "pyramid-set-cookie-httponly-unsafe-value",
#         "ssrf-requests", "sqlalchemy-sql-injection"
#     ],
#     "TC 1": [90, 90, 70, 90, 60, 90, 100, 90, 100, 80],
#     "TC 2": [90, 80, 80, 70, 90, 80, 100, 70, 80, 70],
#     "TC 3": [80, 90, 70, 80, 70, 100, 80, 80, 70, 70],
#     "TC 4": [90, 80, 90, 90, 70, 100, 80, 70, 80, 80],
#     "TC 5": [90, 80, 90, 80, 60, 100, 90, 80, 100, 80],
#     "TC 6": [100, 100, 90, 70, 80, 90, 70, 90, 90, 90],
#     "TC 7": [100, 90, 90, 90, 80, 100, 90, 90, 70, 90],
#     "TC 8": [90, 80, 80, 60, 70, 100, 90, 80, 90, 80],
#     "TC 9": [100, 80, 100, 80, 90, 100, 60, 70, 90, 70],
#     "TC 10": [70, 80, 100, 90, 100, 90, 90, 80, 90, 90]
# }
#
# df = pd.DataFrame(data)
#
#
# df_melted = df.melt(id_vars=["Vulnerability"], var_name="Test Cycle", value_name="Evasion Rate")
#
#
# plt.rcParams.update({
#     'font.size': 12,
#     'font.family': 'Times New Roman',
#     'figure.figsize': (10, 6)
# })
#
#
# sns.boxplot(data=df_melted, x="Vulnerability", y="Evasion Rate", palette="Greys")
#
#
# plt.title("Evasion Rates by Vulnerability Class", fontsize=14)
# plt.xlabel("Vulnerability Details", fontsize=12)
# plt.ylabel("Evasion Rate (%)", fontsize=12)
#
#
# custom_labels = [
#     "regex_dos", "empty-aes-key", "insufficient-dsa-key-size",
#     "disabled-cert-validation", "direct-use-of-jinja2", "avoid-pickle",
#     "request-with-http", "pyramid-set-cookie-\nhttponly-unsafe-value",
#     "ssrf-requests", "sqlalchemy-sql-injection"
# ]
#
#
# plt.xticks(
#     ticks=range(len(custom_labels)),
#     labels=custom_labels,
#     rotation=45,
#     fontsize=11,
#     ha='right'
# )
#
# plt.yticks(fontsize=10)
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.savefig('evasion_rates.png', dpi=300, bbox_inches='tight')
#
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Vulnerability": [
        "regex_dos", "empty-aes-key", "insufficient-dsa-key-size",
        "disabled-cert-validation", "direct-use-of-jinja2", "avoid-pickle",
        "request-with-http", "pyramid-set-cookie-httponly-unsafe-value",
        "ssrf-requests", "sqlalchemy-sql-injection"
    ],
    "TC 1": [10, 10, 30, 10, 40, 10, 0, 10, 0, 20],
    "TC 2": [10, 20, 20, 30, 10, 20, 0, 30, 20, 30],
    "TC 3": [20, 10, 30, 20, 30, 0, 20, 20, 30, 30],
    "TC 4": [10, 20, 10, 10, 30, 0, 20, 30, 20, 20],
    "TC 5": [10, 20, 10, 20, 40, 0, 10, 20, 0, 20],
    "TC 6": [0, 0, 10, 30, 20, 10, 30, 10, 10, 10],
    "TC 7": [0, 10, 10, 10, 20, 0, 10, 10, 30, 10],
    "TC 8": [10, 20, 20, 40, 30, 0, 10, 20, 10, 20],
    "TC 9": [0, 20, 0, 20, 10, 0, 40, 30, 10, 30],
    "TC 10": [30, 20, 0, 10, 0, 10, 10, 20, 10, 10]
}

df = pd.DataFrame(data)


df_melted = df.melt(id_vars=["Vulnerability"], var_name="Test Cycle", value_name="Targeted Detection Rate")


plt.rcParams.update({
    'font.size': 12,
    'font.family': 'Times New Roman',
    'figure.figsize': (10, 6)
})


sns.boxplot(data=df_melted, x="Vulnerability", y="Targeted Detection Rate", palette="Greys")


plt.title("Targeted Detection Rates by Vulnerability Class", fontsize=14)
plt.xlabel("Vulnerability Details", fontsize=12)
plt.ylabel("Detection Rate (%)", fontsize=12)


custom_labels = [
    "regex_dos", "empty-aes-key", "insufficient-dsa-key-size",
    "disabled-cert-validation", "direct-use-of-jinja2", "avoid-pickle",
    "request-with-http", "pyramid-set-cookie-\nhttponly-unsafe-value",
    "ssrf-requests", "sqlalchemy-sql-injection"
]


plt.xticks(
    ticks=range(len(custom_labels)),
    labels=custom_labels,
    rotation=45,
    fontsize=11,
    ha='right'
)

plt.yticks(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('detection_rates.png', dpi=300, bbox_inches='tight')

plt.show()

