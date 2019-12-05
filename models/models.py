from flask import url_for
from frontend import db
from datetime import datetime


class Entry(db.Model):

    # def to_dict(self):
    #     data = {
    #         'id': self.id,
    #         'meanradiusvalue': self.meanradiusvalue,
    #         'meantexturevalue': self.meantexturevalue,
    #         'meanperimetervalue': self.meanperimetervalue,
    #         'meanareavalue': self.meanareavalue,
    #         'meansmoothnessvalue': self.meansmoothnessvalue,
    #         'meancompactnessvalue': self.meancompactnessvalue,
    #         'meanconcavityvalue': self.meanconcavityvalue,
    #         'meanconcavepointsvalue': self.meanconcavepointsvalue,
    #         'meansymmetryvalue': self.meansymmetryvalue,
    #         'meanfractaldimensionvalue': self.meanfractaldimensionvalue,
    #         'radiuserrorvalue': self.radiuserrorvalue,
    #         'textureerrorvalue': self.textureerrorvalue,
    #         'perimetererrorvalue': self.perimetererrorvalue,
    #         'areaerrorvalue': self.areaerrorvalue,
    #         'smoothnesserrorvalue': self.smoothnesserrorvalue,
    #         'compactnesserrorvalue': self.compactnesserrorvalue,
    #         'concavityerrorvalue': self.concavityerrorvalue,
    #         'concavepointserrorvalue': self.concavepointserrorvalue,
    #         'symmetryerrorvalue': self.symmetryerrorvalue,
    #         'fractaldimensionerrorvalue': self.fractaldimensionerrorvalue,
    #         'worstradiusvalue': self.worstradiusvalue,
    #         'worsttexturevalue': self.worsttexturevalue,
    #         'worstperimetervalue': self.worstperimetervalue,
    #         'worstareavalue': self.worstareavalue,
    #         'worstsmoothnessvalue': self.worstsmoothnessvalue,
    #         'worstcompactnessvalue': self.worstcompactnessvalue,
    #         'worstconcavityvalue': self.worstconcavityvalue,
    #         'worstconcavepointsvalue': self.worstconcavepointsvalue,
    #         'worstsymmetryvalue': self.worstsymmetryvalue,
    #         'worstfractaldimensionvalue': self.worstfractaldimensionvalue,
    #         'result': url_for('api.get_result', id=self.id)
    #     }

        # def from_dict(self, data):
        #     for field in ['meanradiusvalue', 'meantexturevalue', 'meanperimetervalue', 'meanareavalue', 'meansmoothnessvalue', 'meancompactnessvalue', 'meanconcavityvalue', 'meanconcavepointsvalue', 'meansymmetryvalue', 'meanfractaldimensionvalue', 'radiuserrorvalue', 'textureerrorvalue', 'perimetererrorvalue', 'areaerrorvalue', 'smoothnesserrorvalue', 'compactnesserrorvalue', 'concavityerrorvalue', 'concavepointserrorvalue', 'symmetryerrorvalue', 'fractaldimensionerrorvalue', 'worstradiusvalue', 'worsttexturevalue', 'worstperimetervalue', 'worstareavalue', 'worstsmoothnessvalue', 'worstcompactnessvalue', 'worstconcavityvalue', 'worstconcavepointsvalue', 'worstsymmetryvalue', 'worstfractaldimensionvalue']:
        #         if field in data:
        #             setattr(self, field, data[field])

    id = db.Column(db.Integer, primary_key=True)
    meanradiusvalue = db.Column(db.Integer, index=True, unique=True)
    meantexturevalue = db.Column(db.Integer, index=True, unique=True)
    meanperimetervalue = db.Column(db.Integer, index=True, unique=True)
    meanareavalue = db.Column(db.Integer, index=True, unique=True)
    meansmoothnessvalue = db.Column(db.Integer, index=True, unique=True)
    meancompactnessvalue = db.Column(db.Integer, index=True, unique=True)
    meanconcavityvalue = db.Column(db.Integer, index=True, unique=True)
    meanconcavepointsvalue = db.Column(db.Integer, index=True, unique=True)
    meansymmetryvalue = db.Column(db.Integer, index=True, unique=True)
    meanfractaldimensionvalue = db.Column(
        db.Integer, index=True, unique=True)
    radiuserrorvalue = db.Column(db.Integer, index=True, unique=True)
    textureerrorvalue = db.Column(db.Integer, index=True, unique=True)
    perimetererrorvalue = db.Column(db.Integer, index=True, unique=True)
    areaerrorvalue = db.Column(db.Integer, index=True, unique=True)
    smoothnesserrorvalue = db.Column(db.Integer, index=True, unique=True)
    compactnesserrorvalue = db.Column(db.Integer, index=True, unique=True)
    concavityerrorvalue = db.Column(db.Integer, index=True, unique=True)
    concavepointserrorvalue = db.Column(
        db.Integer, index=True, unique=True)
    symmetryerrorvalue = db.Column(db.Integer, index=True, unique=True)
    fractaldimensionerrorvalue = db.Column(
        db.Integer, index=True, unique=True)
    worstradiusvalue = db.Column(db.Integer, index=True, unique=True)
    worsttexturevalue = db.Column(db.Integer, index=True, unique=True)
    worstperimetervalue = db.Column(db.Integer, index=True, unique=True)
    worstareavalue = db.Column(db.Integer, index=True, unique=True)
    worstsmoothnessvalue = db.Column(db.Integer, index=True, unique=True)
    worstcompactnessvalue = db.Column(db.Integer, index=True, unique=True)
    worstconcavityvalue = db.Column(db.Integer, index=True, unique=True)
    worstconcavepointsvalue = db.Column(
        db.Integer, index=True, unique=True)
    worstsymmetryvalue = db.Column(db.Integer, index=True, unique=True)
    worstfractaldimensionvalue = db.Column(
        db.Integer, index=True, unique=True)
    result = db.Column(db.Integer, index=True, unique=True)

    date_created = db.Column(db.Integer, default=datetime.utcnow)

    # def __repr__(self):
    #     return '<Entry {}>'.format(self)
