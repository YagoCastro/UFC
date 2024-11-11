from nbconvert.preprocessors import Preprocessor

class CustomCSSPreprocessor(Preprocessor):
    def preprocess(self, nb, resources):
        resources['inlining'] = {'css': open(r"C:\Users\Yago\Desktop\GitHubLocal\UFC\ComputationalIntelligence\HW1\custom.css").read()}
        return nb, resources