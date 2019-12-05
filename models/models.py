from flask import url_for
from frontend.__init__ import db
from datetime import datetime


class Entry(db.Model):

    def to_dict(self):
        data = {
            'id': self.id,
            'meanradiusvalue': self.meanradiusvalue,
            'meantexturevalue': self.meantexturevalue,
            'meanperimetervalue': self.meanperimetervalue,
            'meanareavalue': self.meanareavalue,
            'meansmoothnessvalue': self.meansmoothnessvalue,
            'meancompactnessvalue': self.meancompactnessvalue,
            'meanconcavityvalue': self.meanconcavityvalue,
            'meanconcavepointsvalue': self.meanconcavepointsvalue,
            'meansymmetryvalue': self.meansymmetryvalue,
            'meanfractaldimensionvalue': self.meanfractaldimensionvalue,
            'radiuserrorvalue': self.radiuserrorvalue,
            'textureerrorvalue': self.textureerrorvalue,
            'perimetererrorvalue': self.perimetererrorvalue,
            'areaerrorvalue': self.areaerrorvalue,
            'smoothnesserrorvalue': self.smoothnesserrorvalue,
            'compactnesserrorvalue': self.compactnesserrorvalue,
            'concavityerrorvalue': self.concavityerrorvalue,
            'concavepointserrorvalue': self.concavepointserrorvalue,
            'symmetryerrorvalue': self.symmetryerrorvalue,
            'fractaldimensionerrorvalue': self.fractaldimensionerrorvalue,
            'worstradiusvalue': self.worstradiusvalue,
            'worsttexturevalue': self.worsttexturevalue,
            'worstperimetervalue': self.worstperimetervalue,
            'worstareavalue': self.worstareavalue,
            'worstsmoothnessvalue': self.worstsmoothnessvalue,
            'worstcompactnessvalue': self.worstcompactnessvalue,
            'worstconcavityvalue': self.worstconcavityvalue,
            'worstconcavepointsvalue': self.worstconcavepointsvalue,
            'worstsymmetryvalue': self.worstsymmetryvalue,
            'worstfractaldimensionvalue': self.worstfractaldimensionvalue,
            'result': url_for('api.get_result', id=self.id)
        }


        def from_dict(self, data):
            for field in ['meanradiusvalue', 'meantexturevalue', 'meanperimetervalue', 'meanareavalue', 'meansmoothnessvalue', 'meancompactnessvalue', 'meanconcavityvalue', 'meanconcavepointsvalue', 'meansymmetryvalue', 'meanfractaldimensionvalue', 'radiuserrorvalue', 'textureerrorvalue', 'perimetererrorvalue', 'areaerrorvalue', 'smoothnesserrorvalue', 'compactnesserrorvalue', 'concavityerrorvalue', 'concavepointserrorvalue', 'symmetryerrorvalue', 'fractaldimensionerrorvalue', 'worstradiusvalue', 'worsttexturevalue', 'worstperimetervalue', 'worstareavalue', 'worstsmoothnessvalue', 'worstcompactnessvalue', 'worstconcavityvalue', 'worstconcavepointsvalue', 'worstsymmetryvalue', 'worstfractaldimensionvalue']:
                if field in data:
                    setattr(self, field, data[field])
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    # date_created = db.Column(db.Integer, default=datetime.utcnow)

    # def __repr__(self):
    #     return '<Entry {}>'.format(self.username)
